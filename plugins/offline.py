from pyrogram import Client , Message , Filters
from db import r
import time
import bot

###########  OFFLINE OPTIONS  ###########
@Client.on_message(Filters.private , group=33)
def me (app : Client ,msg : Message):
    me = app.get_me()
    status = me.status
    off_mode = r.get("offmode")
    if status == "offline":

        if off_mode =="on":
            txt = bot.botfullprefix + "Привет, это бот-автоответчик \ud83e\udd16 \nЯ сейчас занят. Просьба не беспокоить \ud83d\udd15 \nСпасибо за понимание \ud83e\udd1d"
            app.send_message(
                msg.chat.id,
                txt,
            )
            return
        else:
            pass
    else:
        pass


@Client.on_message(Filters.me & Filters.regex("^[Oo]fftxt (.*)$"), group=34)
def offline_text (app : Client ,msg : Message):
    txt = msg.text.split(" ")[1:50]
    text = " "
    text = text.join(txt)
    r.set("offtxt" , text)
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        f"**[Multibot]** Добавлен offline текст:\n`{text}`"
        )
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.me & Filters.regex("!offline$"), group=35)
def offline_mode(app : Client ,msg : Message):

    if r.get("offmode") == "on":
        r.set("offmode","off")
        txt = bot.botfullprefix + f"offline-режим `Выкл`"
    else:
        r.set("offmode","on")
        txt = bot.botfullprefix + f"offline-режим `Вкл`"

    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        text = txt
    )
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
