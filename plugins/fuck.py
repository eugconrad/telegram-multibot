from pyrogram import Client , Message , Filters
from db import r
import time
import bot


# ADD FOSH
@Client.on_message(Filters.me & Filters.regex("!addf (.*)"), group=10)
def addfo(app : Client ,msg : Message):
    _ = msg.text.split(" ")[0]
    fo = msg.text.replace(_,"")
    r.sadd("fosh",fo)
    text = bot.botfullprefix + f"Спам-фраза`{fo}`  добавлена"
    app.edit_message_text(msg.chat.id,msg.message_id,text)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

# DEL FOSH
@Client.on_message(Filters.me &  Filters.regex("!delf (.*)"), group=11)
def delfo(app : Client ,msg : Message):
    _ = msg.text.split(" ")[0]
    fo = msg.text.replace(_,"")
    r.srem("fosh",fo)
    text = bot.botfullprefix + f"Спам фраза`{fo}`  удалена"
    app.edit_message_text(msg.chat.id,msg.message_id,text)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


# LIST FOSH
@Client.on_message(Filters.me &  Filters.regex("!listf"), group=12)
def listf(app : Client ,msg : Message):
    fl = r.smembers("fosh")
    text = bot.botfullprefix + f"Доступные спам-фразы:\n  {str(fl)}"
    count = 1
    for i in fl:
        text = text + f"{count} -`{i}`\n"
        count+=1
    app.edit_message_text(msg.chat.id,msg.message_id,text + "\nДобавить:\n`!addf {спам-фраза}`\nУдалить:\n`!delf {спам фраза}`")


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.regex("!clearf$") & Filters.me, group=13)
def clearf(app : Client ,msg : Message):
    r.delete("fosh")
    app.edit_message_text(msg.chat.id,msg.message_id, bot.botfullprefix + "Список спам-фраз очищен")

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
