from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import nekos
import requests
import json
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def neko(update, context):
    nekoI = nekos.img(target='neko')
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=nekoI)

def kitsune(update, context):
    kitI = nekos.img(target='fox_girl')
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=kitI)

def cat(update, context):
    catI = nekos.cat()
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=catI) 

def urban(update, context):
    url= f'https://api.urbandictionary.com/v0/define?term={update.message.text}'
    request = requests.get(url)
    outputJ = json.loads(request.text)
    output = outputJ['definition']
    update.message.reply_text(output)

def AI(update: Update, context: CallbackContext):
    message = update.message.text
    url = requests.get('http://api.brainshop.ai/get?bid=&key=&uid=[666]&msg='+message)
    decode = json.loads(url.text)
    ai = decode['cnt']
    update.message.reply_text(ai)

def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('neko',neko))
    dp.add_handler(CommandHandler('kitsune',kitsune))
    dp.add_handler(CommandHandler('cat',cat))
    dp.add_handler(CommandHandler('urban',urban))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, AI))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()