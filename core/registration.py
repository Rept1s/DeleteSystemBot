from aiogram import F
from aiogram.filters import Command

from core.admin import chats_list, user_list, sender_post_chat, sender_post_user
from core.handlers import start, chat_member_handler, delete_system_message
from core.filters import FilterDirectType, FilterAdmin, FilterGroupType, FilterNewUser, SystemMessageFilter, FilterReply


async def register_reg(dp):
    dp.message.register(chat_member_handler, FilterGroupType(), FilterNewUser())
    dp.message.register(delete_system_message, FilterGroupType(), SystemMessageFilter())

    dp.message.register(chats_list, Command(commands=["list"]), FilterAdmin())
    dp.message.register(user_list, Command(commands=["users"]), FilterAdmin())
    dp.message.register(sender_post_chat, Command(commands=["send_chat"]), FilterAdmin(), FilterReply())
    dp.message.register(sender_post_user, Command(commands=["send_user"]), FilterAdmin(), FilterReply())

    dp.message.register(start, ~F.text.in_(['/send_user', '/send_chat']), FilterDirectType())
