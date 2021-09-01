import re
from . import *

# Credits to @ForGo10God developer of HellBot.
# This is a first plugin of Hellbot owner . He made when he released first HellBot.
# Modified to work in groups with inline mode disabled.
# Added error msg if no voice is found.
# So please dont remove credit. 
#now this plugin in D3VIL USERBOT

@bot.on(mafia_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(mafiakrish):
    mafia = mafiakrish.pattern_match.group(1)
    if not mafia:
        if mafiakrish.is_reply:
            (await mafiakrish.get_reply_message()).message
        else:
            await edit_or_reply(kraken, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(mafia))}")
    if troll:
        await mafiakrish.delete()
        d3vl_ = await troll[0].click(Config.LOGGER_ID)
        if d3vl_:
            await bot.send_file(
                mafiakrish.chat_id,
                d3vl_,
                caption="",
            )
        await d3vl_.delete()
    else:
    	await eod(mafiakrish, "**Error 404:**  Not Found")
    	
@bot.on(mafia_cmd(pattern="meev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="meev(?: |$)(.*)", allow_sudo=True))
async def nope(mafiakrish):
    mafia = mafiakrish.pattern_match.group(1)
    if not mafia:
        if mafiakrish.is_reply:
            (await mafiakrish.get_reply_message()).message
        else:
            await edit_or_reply(kraken, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("Myinstantsbot", f"{(deEmojify(mafia))}")
    if troll:
        await mafiakrish.delete()
        d3vl_ = await troll[0].click(Config.LOGGER_ID)
        if d3vl_:
            await bot.send_file(
                d3vl.chat_id,
                d3vl_,
                caption="",
            )
        await d3vl_.delete()
    else:
    	await eod(mafiakrish, "**Error 404:**  Not Found")


CmdHelp("memevoice").add_command(
	"mev", "<query>", "Searches the given meme and sends audio if found."
).add_command(
	"meev", "<query>", "Same as {hl}mev"
).add_info(
	"Audio Memes."
).add_warning(
	"✅ Harmless Module."
).add()
