import re
import os
from os import environ
from pyrogram import enums
from Script import script
from dotenv import load_dotenv

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

load_dotenv("./dynamic.env", override=True)
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '9dd673fa7291fb5a954902ea10fc8cb5')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/c754e9fdceffbd57ea69e.jpg https://telegra.ph/file/62e07bb72c3a4247e7318.jpg https://telegra.ph/file/a6c7ba79a2046abf693e4.jpg https://telegra.ph/file/61dbab0c79fedd5df4bce.jpg')).split()
APICS = (environ.get('APICS', 'https://telegra.ph/file/3e6e5b25be2bc72c7d3d3.jpg https://telegra.ph/file/204cb2f3e2086cc9e2582.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/60d2e897bfdf063f81545.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://graph.org/file/cd9d7825d4c11195c19df.jpg")
SNO_IMG = environ.get('SNO_IMG',"https://telegra.ph/file/aae41482507312961e5d8.jpg")

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001950095127').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", f"{script.APPROVED_TEXT}")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()
REACTIONS = ["❤️‍🔥", "⚡", "🔥", "🥰", "🤡", "🤩"]

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6552970915').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002457424722 -1002439854017 -1002464786163 -1002347729816 -1002455627116').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Kanhaiya")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Hacker_Jr')
MONGO_URL = os.environ.get('MONGO_URL', "None")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "7"))
S_GROUP = environ.get('S_GROUP',"https://t.me/KLMovieGroup")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/Team_Kl")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+WDeeDdOuQV44NTI9")
MSG_ALRT = environ.get('MSG_ALRT', '⏤͟͟͞ ♡ Nᴀɴᴄʏ ᵛ³')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002237007652'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Team_KL')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#Fsub
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# Dont Change Anything Here
REQ_CHANNEL=environ.get("REQ_CHANNEL", None)
REQ_CHANNEL = (int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False) if REQ_CHANNEL is not None else None
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
