from pyrogram import Client , Message , Filters ,errors
from db import r
import time
import bot

@Client.on_message(Filters.regex("!settings") & Filters.me , group=36)
def settings(app : Client ,msg : Message):
    password = r.get("password")
    password = password[0] + "*" * (len(password) - 2) + password[-1]
    if "ssh" in r.keys():
        ip = r.hgetall("ssh")["ip"][:3]

    else:
        ip = "Сервер не настроен"

    chatid = msg.chat.id
    text = bot.botfullprefix + f"""Настройки:
┏ Активное чат действие: `{r.get("action") or "PLAYING"}`
┣ Режим чат действия: `{r.get("actionmode")}`
┗ Невидимка `{r.get("lastseen")}`
┏ Автоудаление: `{r.get("autodel")}`
┣ Время автоудаления: {r.get("autodeltime")}
┗ Этот чат не отмеченный? `{"Да" if str(chatid) in r.smembers("unmark") else "Нет"}`
┏ Сервер: `{"Подкл" if "ssh" in r.keys() else "Нет подкл"}`
┣ IP: `{ip}`
┗ Пароль: `{"Скрыто" if "ssh" in r.keys() else "Нет подкл"}`
"""
    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
