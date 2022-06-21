# © @always_hungry365
# Owner Mayank
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo



from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from InsaneRobot import telethn as bot
from InsaneRobot import telethn as tgbot
from InsaneRobot.events import register
from InsaneRobot import dispatcher


edit_time = 5
""" =======================Insane====================== """
file1 = "https://telegra.ph/file/c1ca97093abb67d0a315f.jpg"
file2 = "https://telegra.ph/file/1888df0502c912cba05da.jpg"
file3 = "https://telegra.ph/file/b1ad2984cb59d29f40d17.jpg"
file4 = "https://telegra.ph/file/5c1f6ba30b73bed07e618.jpg"
file5 = "https://telegra.ph/file/d7f3f9f0cf5790cf962cc.jpg"
""" =======================Insane====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information",data="informations")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"hello {firstname}, \n Click The Below Button \n To Get Your Info", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LILIE = "POWERED BY @Insane_Help \n\n"
    LILIE += f"FIRST NAME : {PRO.first_name} \n"
    LILIE += f"LAST NAME : {PRO.last_name}\n"
    LILIE += f"YOU BOT : {PRO.bot} \n"
    LILIE += f"RESTRICTED : {PRO.restricted} \n"
    LILIE += f"USER ID : {boy}\n"
    LILIE += f"USERNAME : {PRO.username}\n"
    await event.answer(LILIE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")


__command_list__ = [
    "myinfo"
]


__help__ = """
 *Info generator...*
 - `/myinfo` generate your own info.
"""

__mod_name__ = "ℹ️ ᴍʏɪɴғᴏ"

