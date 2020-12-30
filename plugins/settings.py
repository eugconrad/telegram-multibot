from pyrogram import Client , Message , Filters ,errors
from db import r
import time



@Client.on_message(Filters.regex("^[sS]ettings$") & Filters.me , group=28)
def settings(app : Client ,msg : Message):
    password = r.get("password")
    password = password[0] + "*" * (len(password) - 2) + password[-1]
    if "ssh" in r.keys():
        ip = r.hgetall("ssh")["ip"][:3]

    else:
        ip = "NoServer Seted"

    chatid = msg.chat.id
    text = f"""
\ud83d\udd10 Настройки:

┏ **Чат action:** `{r.get("action") or "PLAYING"}`
┗ Режим: `{r.get("actionmode")}`
┏ **Анти-спам**: `Вкл`
┗ если спам: `Блокировка`
┏ **Пароль:** `{password}`
┣ **Босс:** [{r.get("boss")}](tg://user?id={r.get("boss")})
┣ **Был в сети:** `{r.get("lastseen")}`
┣ **Фильтр:** `{r.get("filterfosh")}`
┗ **Fosh-мейкер:** `{r.get("fmaker")}`
┏ Автоудаление: `{r.get("autodel")}`
┣ Время: {r.get("autodeltime")}
┗ Этот чат не отмеченный? `{"Да" if str(chatid) in r.smembers("unmark") else "Нет"}`
┏ **Сервер**: `{"Подкл" if "ssh" in r.keys() else "Нет подкл"}`
┣ IP: `{ip}***`
┗ Пароль: `{"Скрыто" if "ssh" in r.keys() else "Нет подкл"}`

[Multibot by \ud83c\udf52]

"""
    app.edit_message_text(text=text,
            chat_id=msg.chat.id,
            message_id=msg.message_id,)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
