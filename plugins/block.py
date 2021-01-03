from pyrogram import Client , Message , Filters
from db import r
import time
import bot

@Client.on_message(Filters.me & (Filters.private | Filters.group) & Filters.regex("!ban$") & Filters.reply , group=5)
def block(app : Client ,msg : Message):

    user_id = msg.reply_to_message.from_user.id
    fname = msg.reply_to_message.from_user.first_name

    try:
        app.block_user(
            user_id
        )
        app.edit_message_text(
            message.chat.id,
            message.message_id,
            bot.botfullprefix + f"Юзер [{fname}](tg://user?id={user_id}) заблокирован"
        )
    except:
        pass

@Client.on_message(Filters.me & (Filters.private | Filters.group) & Filters.regex("!unban$") & Filters.reply , group=6)
def ublock (app : Client ,msg : Message):
    user_id = msg.reply_to_message.from_user.id
    fname = msg.reply_to_message.from_user.first_name
    try:
        app.unblock_user(
            user_id
        )
        app.edit_message_text(
            msg.chat.id,
            msg.message_id,
            bot.botfullprefix + f"Юзер [{fname}](tg://user?id={user_id}) разблокирован"
        )
    except:
        pass
