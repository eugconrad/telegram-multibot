from pyrogram import Client , Message , Filters
from db import r
import time

helptext = """
`Multibot by \ud83c\udf52 system help`
\ud83d\udcdd Доступные команды:

help - это сообщение
settings - настройки
boss - доверенный аккаунт
autodel - отключить автоудаление сообщений
autodel (сек) - время автоудаления сообщений

server - инфо сервера
connect - подключиться по ssh к серверу
exit() - отключиться по shh от сервера

today - текущие дата и время
id - узнать id юзера (через ответ)

spam (кол-во) - спам (через ответ)
spamf (кол-во) - спам фразами
addf - добавить фразу для спама
delf - удалить фразу для спама
listf - список фраз для спама
clearf - оичстить список фраз

action - вкл/выкл чат действие
setaction (действие) - установить чат действие
actionlist - список доступных чат действий

set (команда) - установить быструю команду на вложение (через ответ)
cmdlist - список доступных быстрых команд
dcmd (команда) - удалить быструю команду

nobody - никто не видит статус онлайна
everybody - все видят статус онлайна
mark - добавить чат в отмеченные
marklist - список отмеченных чатов
m - заглушить
offline - вкл/выкл режим **Не беспокоить**

d - удалить сообщение (через ответ)
b - заблокировать юзера (через ответ)
ub - разблокировать юзера (через ответ)
pin - закрепить сообщение (через ответ)
unpin - открепить сообщение (через ответ)
kick - кикнуть юзера (через ответ)

**[Multibot by \ud83c\udf52]**
"""
@Client.on_message(Filters.regex("^[hH]elp$") & Filters.me, group=32)
def help(app : Client ,msg : Message):
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        helptext)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
