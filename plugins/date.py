
from pyrogram import Client , Filters , Message
import requests , time
from db import r
import datetime

@Client.on_message(Filters.regex("^[Tt]oday$")& Filters.me)
def today(app : Client , msg : Message):

    text = f"""
\ud83d\udd70 Сейчас на календаре `{datetime.datetime.today().strftime("%d.%m.%Y")}`
Идёт `{int(datetime.datetime.today().strftime("%j"))}` день `{datetime.datetime.today().strftime("%Y")}` года
Текущее время `{datetime.datetime.today().strftime("%H часов %M минут")}`

**[Multibot by \ud83c\udf52]**
    """
    app.edit_message_text(
        chat_id=msg.chat.id,
        message_id=msg.message_id,
        text = text,
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
