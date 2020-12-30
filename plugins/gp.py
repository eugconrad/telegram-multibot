from pyrogram import Client , Message , Filters
from db import r
import time

@Client.on_message(Filters.me &  Filters.group & Filters.reply & Filters.regex("^[Pp]in$") , group=8)
def pin(app : Client ,msg : Message):

    msgid = msg.reply_to_message.message_id
    app.pin_chat_message(msg.chat.id,msgid )
    text = f"**[Multibot]** сообщение закреплено"
    app.edit_message_text(msg.chat.id,msg.message_id,text)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.group & Filters.reply & Filters.regex("^[Uu]npin$") & Filters.me, group=9)
def unpin(app : Client ,msg : Message):

    #msgid = msg.reply_to_message.message_id

    app.unpin_chat_message(msg.chat.id )

    text = f"**[Multibot]** сообщение откреплено"
    app.edit_message_text(msg.chat.id,msg.message_id,text)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.me & Filters.reply & Filters.group &Filters.regex("[Kk]ick"), group=46)
def ck(app : Client ,msg : Message):
    userid = msg.reply_to_message.from_user.id
    fname = msg.reply_to_message.from_user.first_name

    app.kick_chat_member(msg.chat.id,userid)
    text = f"**[Multibot]** Юзер {fname} кикнут из чата"
    app.edit_message_text(msg.chat.id,msg.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
