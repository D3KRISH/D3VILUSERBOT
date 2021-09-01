import asyncio
import datetime

from . import *

@bot.on(mafia_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(mafia):
    if mafia.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(mafia, "`·.·★ ℘ıŋɠ ★·.·´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  __**Oɯɳҽɾ**__ **:**  {mafia_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your Hêllẞø†"
).add_warning(
  "✅ Harmless Module"
).add()

# hellbot
