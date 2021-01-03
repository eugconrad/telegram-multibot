from pyrogram import Client , Message , Filters
from db import r
import time
import bot

@Client.on_message(Filters.me & Filters.regex("!autodel? ?(\d*)$") , group=4)
def autodel(app : Client ,msg : Message):
    if " " in msg.text:
        timer = msg.text.split(" ")[1]
        r.set("autodeltime", timer)
        text = bot.botfullprefix + f"Время автоудаления `{timer}` секунд"
    else:
        if r.get("autodel") == "on":
            r.set("autodel", "off")
            text = bot.botfullprefix + "Автоудаление `Выкл`"
        else:
            r.set("autodel", "on")
            text = bot.botfullprefix + "Автоудаление `Вкл`"

    app.edit_message_text(msg.chat.id,msg.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
