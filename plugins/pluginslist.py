from pyrogram import Client , Message , Filters
from db import r
import time
import bot

pluginstext = bot.botfullprefix + """Плагины и команды:

Временно на доработке!

https://github.com/Conradk10/telegram-multibot/
"""
@Client.on_message(Filters.regex("!plugins$") & Filters.me)
def help(app : Client ,msg : Message):
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        pluginstext)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
