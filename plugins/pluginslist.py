from pyrogram import Client , Message , Filters
from db import r
import time

pluginstext = """
\ud83d\udcdd Плагины и команды:
About:
`about` - о проекте

Action:
`action` - вкл/выкл чат действие
`setaction {action}` - установить чат действие {action}
`actionlist` - список доступных чат действий

Autodel:
`autodel` - вкл/выкл автоудаление сообщений
`autodel {time}` - изменить время {time} автоудаления сообщений в секундах

Block:
`b` - заблокировать юзера (через ответ)
`ub` - разблокировать юзера (через ответ)

Boss:
`boss` - привязать доверенный аккаунт

Cmd:
`set {cmd}` - установить быструю команду {cmd} на вложение (через ответ)
`cmdlist` - список доступных быстрых команд
`dcmd {cmd}` - удалить быструю команду {cmd}

D:
`d` - удалить сообщение (через ответ)

Date:
`today` - текущие дата и время

Fuck:
`addf {text}` - добавить фразу {text} в список фраз (Spam)
`delf {text}` - удалить фразу {text} из сипска фраз (Spam)
`listf` - отобразить список доступных фраз (Spam)
`clearf` - оичстить список доступных фраз (Spam)

Gp:
`pin` - закрепить сообщение (через ответ)
`unpin` - открепить сообщение (через ответ)
`kick` - кикнуть юзера (через ответ)

Help:
`help` - отобразить все доступные команды

Id:
`id` - узнать id юзера (через ответ)

Lastseen:
`nobody` - выключить отображение последнего времени онлайна
`everybody` - включить отображение последнего времени онлайна

Mark:
`mark` - добавить/удалить чат в список отмеченных чатов
`marklist` - отобразить список отмеченных чатов

Mute:
`m` - заглушить (через ответ)

Offline:
`offline` - вкл/выкл режим не беспокоить (когда не в сети)

Pluginslist:
`plugins` - отобразить список плагинов и команд к ним

Run:
`py {script}` - запустить скрипт {scrpit} Python

Server:
`server` - отобразить состояние сервера

Settings:
`settings` - отобразить настройки бота

Spam:
`spam {n}` - спам пересылкой {n} количество раз (через ответ)
`spamf {n}` - спам {n} раз фразами

Ssh:
`connect` - установить соединение по ssh с сервером
`exit()` - разорвать соединение по ssh с сервером

https://github.com/Conradk10/telegram-multibot/
**[Multibot by \ud83c\udf52]**
"""
@Client.on_message(Filters.regex("^[Pp]lugins$") & Filters.me, group=32)
def help(app : Client ,msg : Message):
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        pluginstext)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
