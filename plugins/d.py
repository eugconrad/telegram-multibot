from pyrogram import Client , Message , Filters
from db import r


@Client.on_message(Filters.me & Filters.reply &  Filters.regex("^[Dd]$"),group=14)
def delete(app : Client ,msg = Message):
    msgid = msg.reply_to_message.message_id
    mymsg = msg.message_id
    app.delete_messages(msg.chat.id, [msgid,mymsg])