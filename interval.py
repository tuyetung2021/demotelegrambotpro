from threading import Timer
import time


def hiddenInterval(update, context):
    while True:       
        print("hiddenInterval")
        update.message.reply_text('The Price : '+str(context.args[0]))
        time.sleep(3)