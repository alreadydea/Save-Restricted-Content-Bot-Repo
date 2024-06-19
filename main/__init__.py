#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()

# ggn = "mongodb+srv://viktor55:Gagan@123@cluster0.4efvr6n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

API_ID = "23536615"
API_HASH = "0731650e848c3791823e19eee62b891c"
P_SLvdS2TuiTS-dRlGx_sA9Zgv9FGm8iqMtnlchH-c6WS-9qDSTpcARArGNxkEt-lv9HyfJ0rVc55Irt6aeqGpT8k3DgYID8v2B431WbdrLKLv2UtjoWRWKNbvqoiSIhnkYv_cQE3JYj35Vu9pLmxTJelEN-an09mhMaHMofdwrJMv5IIk2x20lKgN22UD01jo2QMR0NZXPiypVOWGgH5byKtz_QAAAAGrBhh3AA"
FORCESUB = "devggn"
AUTH = "1213231"
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
