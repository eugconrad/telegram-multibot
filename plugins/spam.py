from pyrogram import Client , Message , Filters
from db import r
import time , random

@Client.on_message(Filters.me &  Filters.regex("^[Ss]pam (\d*)$") & Filters.reply , group=21)
def spam(app : Client ,msg : Message):
    msgid = msg.reply_to_message.message_id
    chatid = msg.chat.id
    spam = int(msg.text.split(" ")[1])
    for i in range(spam):
        app.forward_messages(
            chat_id=chatid,
            from_chat_id=chatid,
            message_ids=[msgid]
        )
    app.delete_messages(msg.chat.id,msg.message_id)



@Client.on_message(Filters.regex("^[Ss]pamf (\d*)$") & Filters.me , group=22)
def spamf(app : Client ,msg : Message):
    msg_id = None
    if msg.reply_to_message: msg_id = msg.reply_to_message.message_id

    spam = int(msg.text.split(" ")[1])
    foshes = list(r.smembers("fosh"))
    for i in range(spam):
        fosh = random.choice(foshes)
        app.send_message(msg.chat.id,fosh, reply_to_message_id=msg_id)

    app.delete_messages(msg.chat.id,msg.message_id)
