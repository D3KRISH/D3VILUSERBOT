from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------
d3vil_pic = Config.ALIVE_PIC or "1https://telegra.ph/file/6f84e0cd473892e0c114f.mp4"
alive_c = f"__**🔥🔥∂3vιℓвσт ɨs αℓιvε🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {d3vil_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• D3vιℓẞø†       :  __**{d3vil_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {d3vil_channel}\n"
alive_c += f"•♦• creator      :[∂3vιℓ кяιsн](
#-------------------------------------------------------------------------------

@bot.on(d3vil_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await d3vil.get_chat()
    await d3vil.delete()
    await bot.send_file(d3vil.chat_id, d3vil_pic, caption=alive_c)
    await d3vil.delete()

msg = f"""
**⚡ D3vιℓвσт ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**D3vιℓẞø†  :**  **{d3vil_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(d3vil_cmd(pattern="d3vil$"))
@bot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def hell_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3vilkrish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
