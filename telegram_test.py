from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

updater = Updater(token='token', use_context=True)

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
updater.start_polling()

