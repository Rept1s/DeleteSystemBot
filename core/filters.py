from aiogram.enums import ContentType
from environs import Env
from aiogram.filters import BaseFilter
from aiogram.types import Message, ChatMemberUpdated


class FilterDirectType(BaseFilter):
    """
        Проверяет, является ли чат приватным.
    """
    async def __call__(self, event: Message) -> bool:
        if event.chat.type == 'private':
            return True
        return False


class FilterGroupType(BaseFilter):
    """
        Проверяет, является ли чат приватным.
    """
    async def __call__(self, event: Message) -> bool:
        if event.chat.type in ['group', 'supergroup']:
            return True
        return False


class FilterAdmin(BaseFilter):
    """
        Проверяет, является ли пользователь админом.
    """
    async def __call__(self, event: Message) -> bool:
        for user in Env().list('ADM_ID'):
            if event.from_user.id == int(user):
                return True
        return False


class FilterHidden(BaseFilter):
    """
        Проверяет, является ли сообщение анонимным.
    """
    async def __call__(self, event: ChatMemberUpdated) -> bool:
        if (await event.bot.get_chat(event.chat.id)).has_hidden_members is True:
            return True
        return False


class FilterNotHidden(BaseFilter):
    """
        Проверяет, является ли сообщение анонимным.
    """
    async def __call__(self, event: Message) -> bool:
        if (await event.bot.get_chat(event.chat.id)).has_hidden_members is None:
            return True
        return False


class FilterReply(BaseFilter):
    """
        Проверяет, является ли сообщение ответом.
    """
    async def __call__(self, event: Message) -> bool:
        if event.reply_to_message is None:
            await event.answer("Сообщение должно быть ответом на рассылаемое сообщение.")
            return False
        return True


class FilterNewUser(BaseFilter):
    """
        Проверяет, является ли сообщение системным.
    """
    async def __call__(self, event: Message) -> bool:
        if event.new_chat_members is None:
            return False
        return True


class SystemMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.content_type in {
            ContentType.LEFT_CHAT_MEMBER,
            ContentType.NEW_CHAT_TITLE,
            ContentType.NEW_CHAT_PHOTO,
            ContentType.DELETE_CHAT_PHOTO,
            ContentType.FORUM_TOPIC_CREATED,
            ContentType.FORUM_TOPIC_EDITED,
            ContentType.FORUM_TOPIC_CLOSED,
            ContentType.FORUM_TOPIC_REOPENED,
            ContentType.GENERAL_FORUM_TOPIC_HIDDEN,
            ContentType.GENERAL_FORUM_TOPIC_UNHIDDEN,
            ContentType.PINNED_MESSAGE,
            ContentType.CHANNEL_CHAT_CREATED,
            ContentType.CONNECTED_WEBSITE,
            ContentType.VIDEO_CHAT_SCHEDULED,
            ContentType.VIDEO_CHAT_STARTED,
            ContentType.VIDEO_CHAT_ENDED,
            ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED,
        }
