import os
os.system("pip install telethon")
import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


okvai = input("Enter y/n to continue: ")
if okvai == "y":
    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print(client.session.save())
        client.send_message("me", client.session.save())
        client.send_message("me", "Above is your #D3VILBOT_SESSION \nPaste this string in Heroku Var.\n\n[Team D3VIL](t.me/D3VIL_SUPPORT)")

else:
    print("THANKS TO VISITING MY REPO JOIN FOR QUERY @D3VIL_BOT_SUPPORT")
