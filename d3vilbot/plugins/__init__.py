import datetime
from mafiabot import *
from mafiabot.config import Config
from mafiabot.helpers import *
from mafiabot.utils import *
from mafiabot.random_strings import *
from mafiabot.version import __mafia__
from telethon import version


MAFIA_USER = bot.me.first_name
mafiakrish = bot.uid
MAFIA_mention = f"[{MAFIA_USER}](tg://user?id={mafiakrish})"
mafia_logo = "./mafiabot/resources/pics/mafiabot_logo.jpg"
cjb = "./mafiabot/resources/pics/cjb.jpg"
restlo = "./mafiabot/resources/pics/rest.jpeg"
shuru = "./mafiabot/resources/pics/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
mafia_ver = __mafia__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "MAFIA_SUPPORT"
my_group = Config.MY_GROUP or "MAFIA_BOT_SUPPORT"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/MAFIA_SUPPORT"
mafia_channel = f"[†hê ∂3vιℓᏰø✞]({chnl_link})"
grp_link = "https://t.me/MAFIA_BOT_SUPPORT"
mafia_grp = f"[∂3ϑîℓᏰø✞ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon


