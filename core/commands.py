from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from environs import Env


async def bot_commands(bot):
    commands = [
        BotCommand(command="start", description="Перезапустить бота"),
    ]
    commands_admin = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="list", description="Посмотреть группы"),
        BotCommand(command="users", description="Посмотреть юзеров"),
        BotCommand(command="send_chat", description="Рассылка по группам"),
        BotCommand(command="send_user", description="Рассылка по пользователям"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
    for chat in Env().list('ADM_ID'):
        await bot.set_my_commands(commands_admin, scope=BotCommandScopeChat(chat_id=chat))
