import asyncio
import requests
from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

msg = f"""
**⚡ ℓεgεη∂αяү αғ ∂3vιℓвσт ⚡**

  •        [📑 Repo 📑](https://github.com/D3KRISH/MAFIABot)
  •        [🚀 Deploy 🚀](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FD3KRISH%2FTHE-MAFIABOT&template=https%3A%2F%2Fgithub.com%2FD3KRISH%2FTHE-MAFIABOT)

  •  ©️ {mafia_channel} ™
"""
botname = Config.BOT_USERNAME

@bot.on(mafia_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        mafia = await bot.inline_query(botname, "repo")
        await mafia[0].click(event.chat_id)
        if event.sender_id == teammafia:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(mafia_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or input_str == "text":
        results = await event.client.inline_query(tgbotusername, "mafiabot_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**⚠️ ERROR !!** \nPlease Re-Check BOT_TOKEN & BOT_USERNAME on Heroku.")
    
        if input_str in CMD_LIST:
          string = "Commands found in {}:\n".format(input_str)
          for i in CMD_LIST[input_str]:
              string += "  " + i
              string += "\n"
          await event.edit(string)
        else:
          await event.edit(input_str + " is not a valid plugin!")

@bot.on(mafia_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def mafiabott(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eod(event, "**⚠️ Error !** \nNeed a module name to show plugin info.")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`▶️ `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eod(event, "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string)


