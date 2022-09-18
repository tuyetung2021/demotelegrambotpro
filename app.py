from telegram.ext import Updater
from telegram.ext import  CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import  os
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

#telegram token
TOKEN = os.environ.get("TOKEN")

#commandhandler for start command
def start(update, context):
    msg = "Hi ! Welcome to Demo Telegram Bot Pro."
    context.bot.send_message(update.message.chat.id, msg)
    
def start2(update, context):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Option 1', callback_data='m1')],
              [InlineKeyboardButton('Option 2', callback_data='m2')],
              [InlineKeyboardButton('Option 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

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
    
    dp.add_handler(CommandHandler('start2', start))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
    dp.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

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
