#Github.com/Vasusen-code

from pyrogram import Client

import asyncio

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

Bot = Client("SaveRestricted", bot_token=BOT_TOKEN, api_id=int(API_ID), api_hash=API_HASH)    

async def start_bots():
    try:
        await userbot.start()
        print("Userbot started successfully!")
    except Exception as e:
        print(f"Userbot failed to start: {e}")
        sys.exit(1)

    try:
        await Bot.start()
        print("Pyrogram bot started successfully!")
    except Exception as e:
        print(f"Bot failed to start: {e}")
        sys.exit(1)

    print("All bots are up and running.")
    await asyncio.Event().wait()  # Keep the bot alive

def run_bots():
    asyncio.run(start_bots())
