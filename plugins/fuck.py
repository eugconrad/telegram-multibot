from pyrogram import Client , Message , Filters
from db import r
import time


# ADD FOSH
@Client.on_message(Filters.me & Filters.regex("[Aa]ddf (.*)"), group=5)
def addfo(app : Client ,msg : Message):
    _ = msg.text.split(" ")[0]
    fo = msg.text.replace(_,"")
    r.sadd("fosh",fo)
    text = f"**[Multibot]** Спам-фраза`{fo}` добавлена"
    app.edit_message_text(msg.chat.id,msg.message_id,text)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

# DEL FOSH
@Client.on_message(Filters.me &  Filters.regex("[Dd]elf (.*)"), group=6)
def delfo(app : Client ,msg : Message):
    _ = msg.text.split(" ")[0]
    fo = msg.text.replace(_,"")
    r.srem("fosh",fo)
    text = f"**[Multibot]** Спам фраза`{fo}` удалена"
    app.edit_message_text(msg.chat.id,msg.message_id,text)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


# LIST FOSH
@Client.on_message(Filters.me &  Filters.regex("[Ll]istf"), group=7)
def listf(app : Client ,msg : Message):
    fl = r.smembers("fosh")
    text = "**[Multibot]** Доступные спам-фразы:\n"
    count = 1
    for i in fl:
        text = text + f"**{count}** -`{i}`\n"
        count+=1
    app.edit_message_text(msg.chat.id,msg.message_id,text)


    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.regex("^[Cc]learf$") & Filters.me, group=30)
def clearf(app : Client ,msg : Message):
    r.delete("fosh")
    app.edit_message_text(msg.chat.id,msg.message_id,"**[Multibot]** Список спам-фраз очищен")

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
