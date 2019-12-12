import setup as general
import logging
import httprequest as req
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

error = "I don't know everything, I just know what I know."

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "HanekawaBot here")

def wiki(update, context):
    search = ""
    for keyword in context.args:
        search += "_" + keyword
    serach = search[1:]
    if(search == ""):
        context.bot.send_message(chat_id = update.effective_chat.id, text = error)
        return
    result = req.wikipedia(search)
    if(result != ""):
        context.bot.send_message(chat_id = update.effective_chat.id, text = result)
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = error)

def unknown(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = error)


updater = Updater(token=general.token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

wiki_handler = CommandHandler('wiki', wiki)
dispatcher.add_handler(wiki_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()