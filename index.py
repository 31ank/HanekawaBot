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

def reddit(update, context):
    subreddit = ""
    mode = ""
    if(context.args[0] != ""):
        subreddit = context.args[0]
    try:
        if(context.args[1] == "rising" or context.args[1] == "hot"):
            mode = context.args[1]
    except:
        mode = "rising"
    if(subreddit == ""):
        context.bot.send_message(chat_id = update.effective_chat.id, text = error)
        return
    result = req.redditreq(subreddit, mode)
    if(result[0] != ""):
        context.bot.send_message(chat_id = update.effective_chat.id, text = result[0] + "\n" + result[1])
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

reddit_handler = CommandHandler('r', reddit)
dispatcher.add_handler(reddit_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()