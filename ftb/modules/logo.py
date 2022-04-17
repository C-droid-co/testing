import os
import io
import requests
from io import BytesIO
import re
from requests import get
from pyrogram.types import Message
from wbb import app as bot
from bs4 import *
from pyrogram import filters	
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@bot.on_message(filters.command("logo"))
async def make_logo(_, message):
    imgcaption = f"""
☘️** Logo Created Successfully**
◇───────────────◇
🔥 **Created by** : @Fintech01_bot 
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : @Fintechbots™ 🇳🇬
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to make logo 📸")
    m = await message.reply_text("📸 Creating..")
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    await m.edit("📤 Uploading ...")
    await bot.send_photo(message.chat.id, photo=photo, caption=imgcaption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
    await m.delete()
            
            
@bot.on_message(filters.command("write"))
async def make_logo(_, message):
    imgcaption = f"""
☘️**write Successfully**
◇───────────────◇
🔥 **Created by** :  @Fintech01_bot 
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : @Fintech01_bot ™ 🇳🇬
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to write ✍️")
    m = await message.reply_text("✍️ writeing ..")
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software?write={text}").history[1].url
    await m.edit("📤 Uploading ...")
    await bot.send_photo(message.chat.id, photo=photo, caption=imgcaption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
    await m.delete()

@bot.on_message(filters.command("glogo"))
async def make_logo(_, message):
    imgcaption = f"""
☘️** Logo Created Successfully**
◇───────────────◇
🔥 **Created by** : @Fintech01_bot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : @fintechbots™ 🇳🇬
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please provide a name... 📸")
    m = await message.reply_text("📸 making your logo...")
    text = message.text.split(None, 1)[1]
    req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
    IMG = req.text
    await m.edit("📤 Uploading ...")
    await bot.send_photo(message.chat.id, photo=IMG, caption=imgcaption.format(message.from_user.mention)),
    await m.delete()
