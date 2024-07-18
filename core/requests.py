from core import models
from sqlalchemy import select, insert, delete, func


async def insert_chats(chat_id, name):
    async with models.async_session() as session:
        query = (
            insert(models.Chats)
            .values(chat_id=chat_id, name=name)
        )
        await session.execute(query)
        await session.commit()


async def insert_user(user_id):
    async with models.async_session() as session:
        query = (
            insert(models.Users)
            .values(user_id=user_id)
        )
        await session.execute(query)
        await session.commit()


async def select_chats():
    async with models.async_session() as session:
        query = (
            select(models.Chats.chat_id, models.Chats.name)
            .select_from(models.Chats)
        )
        result = await session.execute(query)
        return result.fetchall()


async def select_users():
    async with models.async_session() as session:
        query = (
            select(func.count())
            .select_from(models.Users)
        )
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def check_user_id(user_id):
    async with models.async_session() as session:
        query = (
            select(models.Users.user_id)
            .select_from(models.Users)
            .filter_by(user_id=user_id)
        )
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def insert_user_id(user_id):
    async with models.async_session() as session:
        query = (
            insert(models.Users)
            .values(user_id=user_id)
        )
        await session.execute(query)
        await session.commit()


async def check_chat_id(chat_id):
    async with models.async_session() as session:
        query = (
            select(models.Chats.chat_id)
            .select_from(models.Chats)
            .filter_by(chat_id=chat_id)
        )
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def insert_chat_id(chat_id, name):
    async with models.async_session() as session:
        query = (
            insert(models.Chats)
            .values(chat_id=chat_id, name=name)
        )
        await session.execute(query)
        await session.commit()


async def all_user_post():
    async with models.async_session() as session:
        query = (
            select(models.Users.user_id)
            .select_from(models.Users)
        )
        result = await session.execute(query)
        return result.fetchall()


async def delete_user_id(user_id):
    async with models.async_session() as session:
        query = (
            delete(models.Users)
            .filter_by(user_id=user_id)
        )
        await session.execute(query)
        await session.commit()


async def all_chat_post():
    async with models.async_session() as session:
        query = (
            select(models.Chats.chat_id)
            .select_from(models.Chats)
        )
        result = await session.execute(query)
        return result.fetchall()


async def delete_chat_id(chat_id):
    async with models.async_session() as session:
        query = (
            delete(models.Chats)
            .filter_by(chat_id=chat_id)
        )
        await session.execute(query)
        await session.commit()


async def get_all_chat_id():
    async with models.async_session() as session:
        query = (
            select(models.Chats.chat_id)
            .select_from(models.Chats)
        )
        result = await session.execute(query)
        return [row[0] for row in result.fetchall()]


async def get_chat_name(chat_id):
    async with models.async_session() as session:
        query = (
            select(models.Chats.name)
            .select_from(models.Chats)
            .filter_by(chat_id=chat_id)
        )
        result = await session.execute(query)
        return result.first()
