
from pyrogram import Client , Filters , Message
import requests , time
from db import r
import datetime

@Client.on_message(Filters.regex("^[Tt]oday$")& Filters.me)
def today(app : Client , msg : Message):

    now = datetime.datetime.today()
    NY = datetime.datetime(2020,1,1)
    d = NY-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)

    text = f"""
\ud83d\udd70 Сейчас на календаре `{datetime.datetime.today().strftime("%d.%m %Y")}`
Текущее время `{datetime.datetime.today().strftime("%H часов %M минут")}`
Идёт `{-d.days}` день `{datetime.datetime.today().strftime("%Y")}` года
До нового года осталось `{d.days+366}` дней `{hh}` часов и `{mm}` минут! \u2603\ufe0f

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
