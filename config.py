

import logging

from telethon import TelegramClient

from os import getenv
from ROYEDITX.data import AVISHA


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 14397330
API_HASH = "80d223dd670503fa6f017359f328cfe3"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)


SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6753033991").split()))
for x in AVISHA:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6753033991"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
