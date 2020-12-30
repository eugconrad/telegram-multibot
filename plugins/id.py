from pyrogram import Client , Message , Filters
from db import r
import time


@Client.on_message(Filters.me  &Filters.reply &  Filters.regex("^([Ii]d)$"))
def id(app : Client, msg : Message):

    uid = msg.reply_to_message.from_user.id

    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        f"**[Multibot]** id юзера: `{uid}`"
    )
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
