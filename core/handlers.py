import logging
from environs import Env
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from core.requests import insert_user_id, check_user_id, check_chat_id, insert_chat_id, delete_chat_id, get_chat_name
from core.settings import settings_all


class StartStop(object):
    def __init__(self, bot):
        self.bot = bot

    async def start_bot(self):
        for admin_id in settings_all().bots.adm_id:
            await self.bot.send_message(admin_id, text="Бот запущен /start ")

    async def stop_bot(self):
        for admin_id in settings_all().bots.adm_id:
            await self.bot.send_message(admin_id, text="Бот остановлен ")


async def start(message: Message):
    if await check_user_id(message.from_user.id) is None:
        await insert_user_id(message.from_user.id)
    await message.answer(
        "👋 <b>Привет! Я бот, который помогает админам групп.</b>\n\n🛡️ <i>Моя главная задача - удалять любые "
        "системные сообщения, в том числе данные о входе и выходе участников. \n\n🔑  Для того, чтобы я работал, "
        "добавьте меня в администраторы группы.\nДля функционирования мне необходимы следующие права: \n"
        "└ Удаление сообщений.</i>\n\n😉 <b>Бот разработан командой:\n 🔗 t.me/GlobalMediaMarket</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='✔️ ДОБАВИТЬ В ГРУППУ', url=Env().str('LINK_BOT_INVITE'))], ]),
        disable_web_page_preview=True)


async def chat_member_handler(message: Message):
    for user_id in [user.id for user in message.new_chat_members]:
        await check_and_insert_chat(message, user_id)
        try:
            await message.bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            logging.error('Не получилось удалить сообщение о входе/выходе: ' + str(message.message_id)
                          + ' имя и id группы: ' + str(message.chat.id) + ' ' + str(message.chat.title) + ' ' + str(e))


async def check_and_insert_chat(message, user_id):
    if user_id == message.bot.id and await check_chat_id(message.chat.id) is None:
        await insert_chat_id(message.chat.id, message.chat.title)
        await message.answer(
            "👋 <b>Привет! Я бот, который помогает админам групп.</b>\n\n🛡️ <i>Моя главная задача - удалять любые "
            "системные сообщения, в том числе данные о входе и выходе участников. \n\n🔑  Для того, чтобы я работал, "
            "добавьте меня в администраторы группы.\nДля функционирования мне необходимы следующие права: \n"
            "└ Удаление сообщений.</i>\n\n😉 <b>Бот разработан командой:\n 🔗 t.me/GlobalMediaMarket</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='✔️ ДОБАВИТЬ В ГРУППУ', url=Env().str('LINK_BOT_INVITE'))], ]),
            disable_web_page_preview=True)
        logging.error('Новая группа: ' + str(message.chat.id) + ' ' + str(message.chat.title))


async def delete_system_message(message: Message):
    try:
        if message.left_chat_member is not None and message.left_chat_member.id == message.bot.id:
            logging.error('Удаление группы: ' + str(message.chat.id) + ' ' + str(message.chat.title))
            return await delete_chat_id(message.chat.id)
        await message.delete()
    except Exception as e:
        logging.error('Не получилось удалить системное сообщение: ' + str(message.message_id) + ' имя и id группы: '
                      + str(message.chat.id) + ' ' + str(message.chat.title) + ' ' + str(e))


async def leave_chat_handler(bot, chat_id):
    try:
        await bot.leave_chat(chat_id)
        logging.error('Покидаю группу: ' + str(chat_id) + ' ' +
                      str((await get_chat_name(chat_id))[0]) + ' ')
    except Exception as e:
        logging.error('Не получилось покинуть группу: ' + str(chat_id) + ' ' +
                      str((await get_chat_name(chat_id))[0]) + ' ' + str(e))
