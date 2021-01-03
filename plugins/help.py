from pyrogram import Client , Message , Filters
from db import r
import time
import bot

helptext = bot.botfullprefix + """Доступные команды:

`!about` - о проекте
`!action` - вкл/выкл чат действие
`!setaction {action}` - установить чат действие {action}
`!actionlist` - список доступных чат действий
`!autodel` - вкл/выкл автоудаление сообщений
`!autodel {time}` - изменить время {time} автоудаления сообщений в секундах
`!ban` - заблокировать юзера (через ответ)
`!unban` - разблокировать юзера (через ответ)
`!setcmd {cmd}` - установить быструю команду {cmd} на вложение (через ответ)
`!cmdlist` - список доступных быстрых команд
`!delcmd {cmd}` - удалить быструю команду {cmd}
`!now` - текущие дата и время
`!addf {text}` - добавить фразу {text} в список фраз (Spam)
`!delf {text}` - удалить фразу {text} из сипска фраз (Spam)
`!listf` - отобразить список доступных фраз (Spam)
`!clearf` - оичстить список доступных фраз (Spam)
`!pin` - закрепить сообщение (через ответ)
`!unpin` - открепить сообщение (через ответ)
`!kick` - кикнуть юзера (через ответ)
`!help` - отобразить все доступные команды
`!userid` - узнать id юзера (через ответ)
`!nobody` - выключить отображение последнего времени онлайна
`!everybody` - включить отображение последнего времени онлайна
`!mark` - добавить/удалить чат в список отмеченных чатов
`!marklist` - отобразить список отмеченных чатов
`!mute` - заглушить (через ответ)
`!offline` - вкл/выкл режим не беспокоить (когда не в сети)
`!plugins` - отобразить список плагинов и команд к ним
`!server` - отобразить системный монитор сервера
`!settings` - отобразить настройки бота
`!spam {n}` - спам пересылкой {n} количество раз (через ответ)
`!spamf {n}` - спам {n} раз фразами
`!connect` - установить соединение по ssh с сервером
`!disconnect` - разорвать соединение по ssh с сервером

https://github.com/Conradk10/telegram-multibot/
"""
@Client.on_message(Filters.regex("!help$") & Filters.me, group=17)
def help(app : Client ,msg : Message):
    app.edit_message_text(
        msg.chat.id,
        msg.message_id,
        helptext)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
