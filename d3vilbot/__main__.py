import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from d3vilbot import LOGS, bot, tbot
from d3vilbot.config import Config
from d3vilbot.utils import load_module
from d3vilbot.version import __d3vil__ as d3vilver
hl = Config.HANDLER
D3VIL_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/cff7f25551e75738ed1b4.jpg"

# let's get the bot ready
async def d3vil_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"D3VILBOT_SESSION - {str(e)}")
        sys.exit()


# d3vilbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("✪ sтαятιηg ∂3vιℓвσт ✪")
            bot.loop.run_until_complete(d3vil_bot(Config.BOT_USERNAME))
            LOGS.info("✪ ∂3vιℓвσт sтαятυρ cσмρℓεтε∂ ✪")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "d3vilbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# let the party begin...
LOGS.info("sтαятιηg вσт мσ∂ε !")
tbot.start()
LOGS.info("⚡ үσυя ∂3vιℓвσт ιs ησω ωσякιηg ⚡")
LOGS.info(
    "нεα∂ тσ @D3VIL_SUPPORT ғσя υρ∂αтεs. αℓsσ נσιη cнαт gяσυρ тσ gεт нεℓρ яεgαя∂ιηg тσ ∂3vιℓвσт."
)

# that's life...
async def d3vil_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                D3VIL_PIC,
                caption=f"#START \n\n∂ερℓσүε∂ ∂3vιℓвσт sυccεssғυℓℓү\n\n**∂3vιℓвσт - {d3vilver}**\n\nType `{hl}ping` or `{hl}alive` тσ cнεcк! \n\nJoin [∂3vιℓвσт Channel](t.me/D3VIL_SUPPORT) ғσя υρ∂αтεs & [∂3vιℓвσт Chat](t.me/D3VIL_BOT_SUPPORT) ғσя αηү qυεяү яεgαя∂ιηg ∂3vιℓвσ†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join D3VILBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@D3VIL_BOT_SUPPORT"))
    except BaseException:
        pass

# Why not come here and chat??
    try:
        await bot(JoinChannelRequest("@D3VIL_SUPPORT"))
    except BaseException:
        pass


bot.loop.create_task(d3vil_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


