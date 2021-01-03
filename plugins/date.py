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

    hour = int(datetime.datetime.today().strftime("%H")) % 10
    minute = int(datetime.datetime.today().strftime("%M")) % 10
    hour_s = "часа"
    minute_s = "минут"

    if hour == 1:
        hour_s = "час"
    elif hour >=2 and hour <= 4:
        hour_s = "часа"
    else:
        hour_s = "часов"

    if minute == 1:
        minute_s = "минута"
    elif minute >= 2 and minute <=4:
        minute_s = "минуты"
    else:
        minute_s = "минут"


    text = bot.botfullprefix + f"""Сегодня `{today}`, на календаре `{datetime.datetime.today().strftime("%d.%m.%Y")}`
Идёт `{int(datetime.datetime.today().strftime("%j"))}` день `{datetime.datetime.today().strftime("%Y")}` года
Текущее время `{datetime.datetime.today().strftime("%H")}` {hour_s} `{datetime.datetime.today().strftime("%M")}` {minute_s} """
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
