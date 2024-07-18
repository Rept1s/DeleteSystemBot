import logging
import asyncio

from core.autoposting import launch_scheduler_post, SchedulerManager
from core.commands import bot_commands
from core.handlers import StartStop
from core.models import async_main
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from core.settings import settings_all
from core.registration import register_reg
from aiogram.client.default import DefaultBotProperties


class StartBot(object):
    def __init__(self):
        self.bot = Bot(
            token=settings_all().bots.token,
            default=DefaultBotProperties
            (parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()

    async def main_bot(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.error('Запускаю бота... ')
        self.dp.startup.register(StartStop(self.bot).start_bot)
        self.dp.shutdown.register(StartStop(self.bot).stop_bot)

        SchedulerManager.get_scheduler()
        await launch_scheduler_post(self.bot)
        await register_reg(self.dp)
        await bot_commands(self.bot)
        await async_main()

        try:
            await self.dp.start_polling(self.bot)  # Ожидание до прерывания
        finally:
            await self.bot.session.close()


if __name__ == '__main__':
    asyncio.run(StartBot().main_bot())
