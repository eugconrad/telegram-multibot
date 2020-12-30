from pyrogram import Client , Message , Filters
from db import r
import time

@Client.on_message(Filters.regex("^[Aa]ction$") & Filters.me)
def action(app : Client ,msg : Message):

    chatid = msg.chat.id

    if str(chatid) in r.smembers("chataction"):
        r.srem("chataction", str(chatid))
        text = "**[Multibot]** Чат действия `Выкл`"
    else:
        r.sadd("chataction", str(chatid))
        text = "**[Multibot]** Чат действия `Вкл`"

    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.incoming,group = 24)
def incoming(app : Client ,msg : Message):
    # DEFULT PLAYING
    action = r.get("action") or "playing"
    chatid = msg.chat.id
    if str(chatid) in r.smembers("chataction"):

        for i in range(3):
            app.send_chat_action(
                chatid,
                action
            )

### SET ACTION
@Client.on_message(Filters.regex("^[Ss]etaction (.*)$") & Filters.me , group=0)
def setaction(app : Client ,msg : Message):
    action = str(msg.text.split(" ")[1])
    r.set("action", action)
    app.edit_message_text(text=f"**[Multibot]** `Чат действие установлено на:` {action}",
            chat_id=msg.chat.id,
            message_id=msg.message_id,)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)



@Client.on_message(Filters.regex("^[Aa]ctionlist$") & Filters.me , group=1)
def actionlist(app : Client ,msg : Message):
    text = """
\ud83d\udcdd Список доступных чат действий:

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
setaction [действие]

**[Multibot by \ud83c\udf52]**
"""

    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
