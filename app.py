from telegram.ext import Updater
from telegram.ext import  CommandHandler, MessageHandler, Filters
import  os
import json

#telegram token
TOKEN = os.environ.get("TOKEN")

#commandhandler for start command
def start(update, context):
    msg = "Hi ! Welcome to Demo Telegram Bot Pro."
    context.bot.send_message(update.message.chat.id, msg)
    
    
#Error handler
def error(update, context):
    context.bot.send_message(update.message.chat.id, "Oops! Error encountered!")

def sum(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1+number2
        update.message.reply_text('The sum is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')
       
def minus(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1-number2
        update.message.reply_text('The minus is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def mul(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1*number2
        update.message.reply_text('The minus is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')
        
def div(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1/number2
        update.message.reply_text('The minus is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')    
        
#main logic
def main():
    
    #to get the updates from bot
    updater = Updater(token=TOKEN, use_context=True)
    
    #to dispatch the updates to respective handlers
    dp = updater.dispatcher
    
    #handlers
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("sum", sum))
    dp.add_handler(CommandHandler("minus", minus))
    dp.add_handler(CommandHandler("mul", mul))
    dp.add_handler(CommandHandler("div", div))

    #dp.add_handler(MessageHandler(Filters.text, mimic))


    dp.add_error_handler(error)
    
    #to start webhook
    updater.start_webhook(listen="0.0.0.0",port=os.environ.get("PORT",443),
                          url_path=TOKEN,
                          webhook_url="https://demo-telegram-bot-pro.herokuapp.com/"+TOKEN)
    updater.idle()

#start application with main function
#name
if __name__ == '__main__':
    main()
