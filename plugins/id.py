from pyrogram import Client , Message , Filters
from db import r
import time
import bot

@Client.on_message(Filters.me  & Filters.reply &  Filters.regex("!userid"))
def id(app : Client, msg : Message):

    uid = msg.reply_to_message.from_user.id

    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        bot.botfullprefix + f"id юзера: `{uid}`"
    )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


# @Client.on_message(Filters.me & Filters.regex("!chatid"))
# def chatid(app : Client, msg : Message):
#
#     app.edit_message_text(
#         msg.chat.id,
#         msg,message_id,
#         f"{msg.chat.id}"
#     )
#
#     if r.get("autodel") == "on":
#             time.sleep(float(r.get("autodeltime")))
#             app.delete_messages(msg.chat.id,msg.message_id)
