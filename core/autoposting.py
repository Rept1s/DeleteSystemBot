import datetime
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from environs import Env

from core.handlers import leave_chat_handler
from core.requests import all_chat_post, get_chat_name, delete_chat_id


class SchedulerManager:
    _scheduler = None

    @classmethod
    def get_scheduler(cls):
        if cls._scheduler is None:
            cls._scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
            cls._scheduler.start()
        return cls._scheduler

    @classmethod
    async def add_job(cls, func, trigger, **kwargs):
        scheduler = cls.get_scheduler()
        scheduler.add_job(func, trigger, **kwargs)

    @classmethod
    async def stop_scheduler(cls):
        if cls._scheduler and cls._scheduler.running:
            cls._scheduler.shutdown(wait=False)
            cls._scheduler = None


async def launch_scheduler_post(bot):
    await SchedulerManager.add_job(
        autopost_message,
        'cron',
        hour=Env().int('TIME_POST'),
        start_date=datetime.datetime.now(),
        kwargs={'bot': bot})
    logging.error('Публикации запланированы')


async def autopost_message(bot):
    for chat_id in [chat_id for chat_id in await all_chat_post() if chat_id]:
        try:
            await bot.copy_message(chat_id=chat_id[0], from_chat_id=Env().str('FROM_CHAT'),
                                   message_id=Env().int('MSG_ID'))
        except Exception as e:
            logging.error('Не получилось публиковать сообщение в группу: ' + str(chat_id[0]) + ' ' +
                          str((await get_chat_name(chat_id[0]))[0]) + ' ' + str(e))
            await leave_chat_handler(bot, chat_id[0])
            await delete_chat_id(chat_id[0])
