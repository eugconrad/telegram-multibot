from pyrogram import Client , Message , Filters
from db import r
import time


@Client.on_message(Filters.me & (Filters.private | Filters.group) & Filters.regex("^[Bb]$") & Filters.reply , group=0)
def block(app : Client ,msg : Message):

    user_id = msg.reply_to_message.from_user.id
    fname = msg.reply_to_message.from_user.first_name
    #f"{count} - [{i}](tg://user?id={i})\n"
    try:
        app.block_user(
            user_id
        )
        app.edit_message_text(
            message.chat.id,
            message.message_id,
            f"**[Multibot]** Юзер [{fname}](tg://user?id={user_id}) заблокирован"
        )
    except:
        pass

@Client.on_message(Filters.me & (Filters.private | Filters.group) & Filters.regex("^[Uu]b$") & Filters.reply , group=1)
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
            f"**[Multibot]** Юзер [{fname}](tg://user?id={user_id}) разблокирован"
        )
    except:
        pass
