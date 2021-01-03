from pyrogram import Client , Filters , Message
import requests , time
from db import r
import datetime
import bot


@Client.on_message(Filters.regex("!now$")& Filters.me)
def today(app : Client , msg : Message):
    weekday = datetime.datetime.today().weekday()
    if weekday == 0:
        today = "понедельник"
    elif weekday == 1:
        today = "вторник"
    elif weekday == 2:
        today = "среда"
    elif weekday == 3:
        today = "четверг"
    elif weekday == 4:
        today = "пятница"
    elif weekday == 5:
        today = "суббота"
    elif weekday == 6:
        today = "воскресенье"

    text = bot.botfullprefix + f"""Сегодня `{today}`, на календаре `{datetime.datetime.today().strftime("%d.%m.%Y")}`
Идёт `{int(datetime.datetime.today().strftime("%j"))}` день `{datetime.datetime.today().strftime("%Y")}` года
Текущее время `{datetime.datetime.today().strftime("%H")}` часов `{datetime.datetime.today().strftime("%M")}` минут"""
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
