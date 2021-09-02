import cv2
import os
import io
import random
import shutil
import re
import textwrap
import lottie

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

from . import *


path = "./mafiamify/"
if not os.path.isdir(path):
    os.makedirs(path)


@bot.on(mafia_cmd(pattern="mmf ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mmf ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, "You need to reply to an image with .mmf` 'text on top' ; 'text on bottom'")
        return
    await eor(event, "🤪 **Memifying...**")
    reply = await event.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("himanshu.webp", semx)
    text = event.pattern_match.group(1)
    webp_file = await draw_meme_text("himanshu.webp", text)
    await event.client.send_file(
        event.chat_id, webp_file, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    shutil.rmtree(path)
    os.remove("mafia.webp")
    os.remove(webp_file)


@bot.on(mafia_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def sed(mafiaboy):
    if mafiaboy.fwd_from:
        return
    if not mafiaboy.reply_to_msg_id:
        await eod(mafiaboy, "You need to reply to an image with .mms` 'text on top' ; 'text on bottom'")
        return
    await eor(mafiaboy, "🤪 **Memifying...**")
    reply = await mafiaboy.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("himanshu.webp", semx)
    text = mafiaboy.pattern_match.group(1)
    photo = await draw_meme("himanshu.webp", text)
    await mafiaboy.client.send_file(
        mafiaboy.chat_id, photo, reply_to=mafiaboy.reply_to_msg_id
    )
    await mafiaboy.delete()
    shutil.rmtree(path)
    os.remove("mafia.webp")
    os.remove(photo)
    
@bot.on(mafia_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(himanshu):
    mafia = himanshu.pattern_match.group(1)
    if not mafia:
        if himanshu.is_reply:
            (await himanshu.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(himanshu, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(himanshu, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(mafia))}")
    if troll:
        await himanshu.delete()
        d3vl_ = await troll[0].click(Config.LOGGER_ID)
        if d3vl_:
            await bot.send_file(
                himanshu.chat_id,
                d3vl_,
                caption="",
            )
        await d3vl_.delete()
    else:
     await eod(himanshu, "Error 404:  Not Found")
     
    
CmdHelp("memify").add_command(
  "mmf", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in sticker format.", "mmf <reply to a img/stcr/gif> hii ; mafiao"
).add_command(
  "mms", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in image format.", "mms <reply to a img/stcr/gif> hii ; mafiao"
).add_command(
  "doge", "<text>", "Makes A Sticker of Doge with given text."
).add_info(
  "Make Memes on telegram 😉"
).add_warning(
  "✅ Harmless Module."
).add()
