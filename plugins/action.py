from pyrogram import Client , Message , Filters
from db import r
import bot
import time

# Вкл/выкл Action
@Client.on_message(Filters.regex("!action") & Filters.me, group = 1)
def action(app : Client ,msg : Message):

    chatid = msg.chat.id
    action = r.get("action")
    
    if str(chatid) in r.smembers("chataction"):
        r.srem("chataction", str(chatid))
        text = bot.botfullprefix + "Чат действия `Выкл`"
    else:
        r.sadd("chataction", str(chatid))
        text = bot.botfullprefix + f"Чат действия `Вкл`\nАктивное чат действие: `{action}`"

    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.incoming, group = 1)
def incoming(app : Client ,msg : Message):
    action = r.get("action") or "playing"
    chatid = msg.chat.id
    if str(chatid) in r.smembers("chataction"):
        for i in range(3):
            app.send_chat_action(
                chatid,
                action
            )

# Установить Action
@Client.on_message(Filters.regex("!setaction (.*)$") & Filters.me, group = 2)
def setaction(app : Client ,msg : Message):
    action = str(msg.text.split(" ")[1])
    r.set("action", action)
    app.edit_message_text(text=bot.botfullprefix + f"Чат действие установлено на: `{action}`",
            chat_id=msg.chat.id,
            message_id=msg.message_id,)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

# Отобразить список доступынх Action
@Client.on_message(Filters.regex("!actionlist") & Filters.me, group = 3)
def actionlist(app : Client ,msg : Message):
    action = r.get("action")
    text = bot.botfullprefix + """Список доступных чат действий:

`typing` - печатает...
`upload_photo` - отправляет фото
`upload_video` - отправляет видео
`record_audio` - записывает голосовое...
`upload_audio` - записывает голосовое...
`upload_document` - отправляет файл
`find_location` - ?
`record_video_note` - записывает видео
`upload_video_note` - записывает видео
`choose_contact` - ?
`playing` - играет в игру

Установить:
`!setaction` {действие}

""" + f"Установленное чат действие: `{action}`"
    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
