#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6092734790:AAHqffUKUi1qVBM5awbdpMxwTGT5Iz48n68")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26376042"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1f5343b0646645ca1eaf7c4759fc248f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001885067474"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2036803347"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://userbot:userbot@cluster0.ltasu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001936280485"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗪𝗲𝗹𝗰𝗼𝗺𝗲 {first}\n\n𝗧𝗼 𝗢𝘂𝗿 𝗙𝗶𝗹𝗲 𝗦𝗵𝗮𝗿𝗲 𝗕𝗼𝘁 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗬𝗼𝘂 𝗔𝗻𝗶𝗺𝗲 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗗𝗲𝗹𝗮𝘆 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 : @Anime_Sensei_Network ❤️.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6066177103").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group @Anime_Sensei_Network to use me ❤️\n\nKindly Please join The Channel And Try again</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "I am a private file share bot! only working for @Anime_Sensei_Network"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
