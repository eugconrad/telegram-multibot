from pyrogram import Client , Message , Filters
from db import r
import time
import bot

# Auto Seen
@Client.on_message(Filters.incoming & Filters.private, group=19)
def autoseen(app : Client ,msg : Message):
    chatid = str(msg.chat.id)
    if chatid in r.smembers("mark"):
        app.read_history(
            chatid
        )

@Client.on_message(Filters.me & Filters.private & Filters.regex("!mark$") , group=20)
def addmark(app : Client ,msg : Message):
    chatid = str(msg.chat.id)
    if chatid in r.smembers("mark"):
        r.srem("mark", chatid)
        text = bot.botfullprefix + "Чат удалён из отмеченных"
    else:
        r.sadd("mark", chatid)
        text = bot.botfullprefix + "Чат успешно добавлен в отмеченные"
    send =app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(msg.chat.id,[send.message_id])


@Client.on_message(Filters.me & Filters.regex("!marklist$") , group=21)
def marklist(app : Client ,msg : Message):
    marklist = r.smembers("mark")
    text = bot.botfullprefix + "Список отмеченных чатов:\n"
    count = 1
    for i in marklist:
        text = text + f"**{count}** - [{i}](tg://user?id={i})\n"
        count+=1
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        text
    )
