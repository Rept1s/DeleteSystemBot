from environs import Env
from dataclasses import dataclass


@dataclass
class Webhook:
    url: str
    key: str
    port: int
    host: str
    patch: str
    certificate: str


@dataclass
class Bots:
    token: str
    adm_id: int


@dataclass
class Settings:
    bots: Bots
    webhook: Webhook


@dataclass
class Database:
    base: str


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            token=env.str("TOKEN"),
            adm_id=env.list("ADM_ID")
        ),
        webhook=Webhook(
            url=env.str("WEBHOOK_URL"),
            key=env.str("WEBHOOK_KEY"),
            port=env.int("WEBHOOK_PORT"),
            host=env.str("WEBHOOK_HOST"),
            patch=env.str("WEBHOOK_PATCH"),
            certificate=env.str("WEBHOOK_CERTIFICATE")
        )
    )


def get_database():
    env = Env()
    env.read_env('input')

    return Database(base=env.str("DB_PATCH"))


def settings_all():
    return get_settings('../input')
