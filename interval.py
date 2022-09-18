from threading import Timer
import time


def hidden(update, context):
    while True:       
        update.message.reply_text('The Price : '+str(context.args[0]))
        time.sleep(3)