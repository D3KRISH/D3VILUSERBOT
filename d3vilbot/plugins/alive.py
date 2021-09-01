from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------
mafia_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
alive_c = f"__**🔥🔥∂3vιℓвσт ɨs αℓιvε🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {mafia_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• D3vιℓẞø†       :  __**{mafia_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {mafia_channel}\n"
alive_c += f"•♦• creator      :[∂3vιℓ кяιsн](
#-------------------------------------------------------------------------------

@bot.on(mafia_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await mafia.get_chat()
    await mafia.delete()
    await bot.send_file(mafia.chat_id, mafia_pic, caption=alive_c)
    await mafia.delete()

msg = f"""
**⚡ D3vιℓвσт ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**D3vιℓẞø†  :**  **{mafia_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(mafia_cmd(pattern="mafia$"))
@bot.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
async def hell_a(event):
    try:
        mafia = await bot.inline_query(botname, "alive")
        await mafia[0].click(event.chat_id)
        if event.sender_id == himanshu:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "mafia", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
