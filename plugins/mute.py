
from pyrogram import Client , Message , Filters
from db import r
import time

mutes = [
    "text",
    "photo",
    "sticker",
    "gif",
    "voice",
    "media",
    "audio",
    "doc",
    "video",
    "vn",
]

@Client.on_message(Filters.me & (Filters.group|Filters.private) & Filters.reply  & Filters.regex("^[Mm] (.*)$") , group =1)
def mute(app : Client ,msg : Message):
    m = msg.text.split(" ")[1]
    fname = msg.reply_to_message.from_user.first_name
    userid = msg.reply_to_message.from_user.id
    if not m in mutes:return
    if str(userid) in r.smembers("mute"+m):
        r.srem("mute"+m,str(userid))
        text = f"**[Multibot]** `{m}` теперь не заглушен для `{fname}`"
    else:
        r.sadd("mute"+m,str(userid))
        text = f"**[Multibot]** `{m}` теперь заглушен для `{fname}`"

    app.edit_message_text(msg.chat.id,msg.message_id,text)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


#@Client.on_message(Filters.me & Filters.regex("[Mm]utelist") , group=12)
#def mutelist(app : Client , msg : Message):


@Client.on_message(Filters.media & (Filters.group|Filters.private), group =2)
def media(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"mutemedia"):return
    app.delete_messages(chatid,msg.message_id)


@Client.on_message(Filters.audio & (Filters.group|Filters.private), group=3)
def audio(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"muteaudio"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.document & (Filters.group|Filters.private),group=4)
def document(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"mutedoc"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.video & (Filters.group|Filters.private), group=5)
def video(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"mutevideo"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.video_note & (Filters.group|Filters.private), group=6)
def video_note(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"mutevn"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.animation & (Filters.group|Filters.private), group=7)
def gif(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers("mutegif"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.voice & (Filters.group|Filters.private), group=8)
def voice(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers("mutevoice"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.photo & (Filters.group|Filters.private), group=9)
def photo(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers("mutephoto"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.sticker & (Filters.group|Filters.private), group=10)
def sticker(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    #print("done")
    if str(userid) not in r.smembers(f"mutesticker"):return
    app.delete_messages(chatid,msg.message_id)

@Client.on_message(Filters.text & (Filters.group|Filters.private), group=11)
def text(app : Client ,msg : Message):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if str(userid) not in r.smembers(f"mutetext"):return
    app.delete_messages(chatid,msg.message_id)
