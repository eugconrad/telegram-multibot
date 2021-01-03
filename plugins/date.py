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

    hour = int(datetime.datetime.today().strftime("%H"))
    minute = int(datetime.datetime.today().strftime("%M"))
    hour_s = "часа"
    minute_s = "минут"

    if hour == 1 or hour == 21:
        hour_s = "час"
    elif hour >=2 and hour <= 4 or hour >= 22 and hour <= 24:
        hour_s = "часа"
    else:
        hour_s = "часов"

    if minute == 1 or minute == 21 or minute == 31 or minute == 41 or minute == 51:
        minute_s = "минута"
    elif minute >= 2 and minute <= 4 or minute >= 22 and minute <= 24 or minute >= 32 and minute <= 34 or minute >= 42 and minute <= 44 or minute >= 52 and minute <= 54:
        minute_s = "минуты"
    elif minute == 0 or minute >= 5 and minute <= 20 or minute >= 25 and minute <= 30 or minute >= 35 and minute <= 40 or minute >= 45 and minute <= 50 or minute >= 55 and minute <= 60:
        minute_s = "минут"



    text = bot.botfullprefix + f"""Сегодня `{today}`, на календаре `{datetime.datetime.today().strftime("%d.%m.%Y")}`
Идёт `{int(datetime.datetime.today().strftime("%j"))}` день `{datetime.datetime.today().strftime("%Y")}` года
Текущее время `{hour}` {hour_s} `{minute}` {minute_s} """
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
