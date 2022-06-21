# © @always_hungry365
# Owner Mayank


import random
from InsaneRobot import telethn as tbot
from telethon import events

@tbot.on(events.NewMessage(pattern="/wish"))
async def wish(Insane):
   if Insane.is_reply:
         mm = random.randint(1,100)
         lol = await Insane.get_reply_message()
         await tbot.send_message(Insane.chat_id, f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol)
   if not Insane.is_reply:
         mm = random.randint(1,100)
         Insane = "https://telegra.ph/file/d7f3f9f0cf5790cf962cc.jpg"
         await tbot.send_file(Insane.chat_id, Insane,caption=f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=Insane)
         lol = await Insane.get_reply_message()
         await tbot.send_file(Insane.chat_id, f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol, file=Insane)
   if not Insane.is_reply:
         mm = random.randint(1,100)
         Insane = "https://telegra.ph/file/d930a4a58831961756ac9.jpg"
         await tbot.send_file(Insane.chat_id,f"**Your wish has been cast.✨**\n\n__chance of success {mm}%__", reply_to=lol, file=Insane)
         await tbot.send_file(Insane.chat_id, Insane,caption=f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=Insane)
         lol = await Insane.get_reply_message()
         await tbot.send_file(Insane.chat_id, f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=lol)
   if not Insane.is_reply:
         mm = random.randint(1,100)
         Insane = "https://telegra.ph/file/c1ca97093abb67d0a315f.jpg"
         await tbot.send_file(Insane.chat_id, Insane,caption=f"**Your wish has been cast.✨**\n__chance of success {mm}%__", reply_to=lol,file=Insane)

        
   
        #Trying To Be A 𝗥𝗮𝗶𝗻𝗯𝗼𝘄 In Someone’s 𝗖𝗹𝗼𝘂𝗱.👉 @Give_Me_Heart
