from threading import Timer
import time


def hiddenInterval(update, context):
    while True:       
        print("hiddenInterval")
        time.sleep(3)