import asyncio
import logging
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.handlers import leave_chat_handler
from core.requests import select_users, select_chats, all_user_post, delete_user_id, delete_chat_id, all_chat_post, \
    get_chat_name


async def chats_list(message: Message, state: FSMContext):
    await message.answer("Группы: \n\n" + str(await select_chats()))


async def user_list(message: Message, state: FSMContext):
    await message.answer("Пользователи: \n\n" + str(await select_users()))


async def sender_post_user(message: Message, state: FSMContext):
    successful_count = 0
    for user_id_tuple in await all_user_post():
        user_id = user_id_tuple[0]
        try:
            await message.bot.copy_message(chat_id=int(user_id), from_chat_id=message.chat.id,
                                           message_id=message.reply_to_message.message_id)
            successful_count += 1
            await asyncio.sleep(2)
        except Exception as e:
            logging.error('Ошибка при отправке сообщения пользователю ' + str(user_id) + ': ' + str(e))
            await delete_user_id(user_id)
    total_users = len(await all_user_post())
    await message.bot.send_message(message.chat.id, 'Рассылка завершена. Сообщения успешно отправлены '
                                   + str(successful_count) + '/' + str(total_users) + ' пользователям.')


async def sender_post_chat(message: Message, state: FSMContext):
    successful_count = 0
    for chat_id_tuple in await all_chat_post():
        chat_id = chat_id_tuple[0]
        try:
            await message.bot.copy_message(chat_id=int(chat_id), from_chat_id=message.chat.id,
                                           message_id=message.reply_to_message.message_id)
            successful_count += 1
            await asyncio.sleep(2)
        except Exception as e:
            logging.error('Ошибка при отправке сообщения в группу ' + str(chat_id) + ' '
                          + str((await get_chat_name(chat_id))[0]) + ': ' + str(e))
            await leave_chat_handler(message.bot, chat_id)
            await delete_chat_id(chat_id)
    total_users = len(await all_chat_post())
    await message.bot.send_message(message.chat.id, 'Рассылка завершена. Сообщения успешно отправлены '
                                   + str(successful_count) + '/' + str(total_users) + ' пользователям.')
