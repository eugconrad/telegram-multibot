import schedule
import time
from pyrogram import Client , Message , Filters


def play_dick(app : Client ,msg : Message):
    app.send_message("me", "**[Multibot]** DickGame модуль активирован")
    sleep(2)
    #app.send_message(-1001249794117, "/dick@kraft28_bot") #FIT floodilka
    sleep(2)
    #app.send_message(-1001375455741, "/dick@kraft28_bot") #Dream house

schedule.every().day.at("23:36").do(play_dick)
schedule.every(10).minutes.do(play_dick)
schedule.run_pending()
print("Модуль DickGame запущен!")

# while True:
#     schedule.run_pending()
#     time.sleep(1)
