from telegram.ext import Updater
from telegram.ext import  CommandHandler, MessageHandler, Filters
import  os
import json

#telegram token
TOKEN = os.environ.get("TOKEN")

#commandhandler for start command
def start(update, context):
    print(start)
    #yourname = update.message.chat.first_name
    msg = "Hi ! Welcome to Milion bot."
    context.bot.send_message(update.message.chat.id, msg)
    

#Message handler for texts only
def mimic(update, context):
    print("mimic")
    context.bot.send_message(update.message.chat.id, update.message.text)

def p(update, context):
    print("p")
    #print("update" + update)
    print("context.args" + context.args)
    context.bot.send_message(update.message.chat.id, update.message.text)

    
#commandhandler for details command
def details(update, context):
    context.bot.send_message(update.message.chat.id, str(update))

#Error handler
def error(update, context):
    context.bot.send_message(update.message.chat.id, "Oops! Error encountered!")

#main logic
def main():
    
    #to get the updates from bot
    updater = Updater(token=TOKEN, use_context=True)
    
    #to dispatch the updates to respective handlers
    dp = updater.dispatcher
    
    #handlers
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("details", details))
    dp.add_handler(CommandHandler("p", p))

    #dp.add_handler(MessageHandler(Filters.text, mimic))


    dp.add_error_handler(error)
    
    #to start webhook
    updater.start_webhook(listen="0.0.0.0",port=os.environ.get("PORT",443),
                          url_path=TOKEN,
                          webhook_url="https://mimic-appli.herokuapp.com/"+TOKEN)
    updater.idle()

#start application with main function
#name
if __name__ == '__main__':
    main()
