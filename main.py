TOKEN = 'PASTEtokenHERE'

import NekoMimi as nm
print(nm.banner('Celestia'))

print('Starting Celestia Telegram\n')

print("Loading PyLibraries . . . ")
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import nekos
import requests
import json
import logging
from googlesearch import search
from RedditReader import Subreddit
print('[ ok ]\n')

print('Loading Neko Functions . . . ')
def filter(msg):
    filt = msg.message.text
    filts = filt.split(' ')
    filters = ''
    for a in filts:
        if not a.startswith('/'):
            filters = filters + a + ' '
    return filters
    
def send(ctx,msg):
    ctx.message.reply_text(msg)
    
def sendImg(updt,ctx,img):
    ctx.bot.send_photo(chat_id=updt.effective_chat.id,photo=img)
    
def addCom(dp,name,com):
    dp.add_handler(CommandHandler(name,com))

print('[ ok ]\n')


print('Starting Bot . . . \n')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def neko(update, context):
    nekoI = nekos.img(target='neko')
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=nekoI)

def kitsune(update, context):
    kitI = nekos.img(target='fox_girl')
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=kitI)

def cat(update, context):
    catI = nekos.cat()
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=catI) 

def fact(update,context):
    fact = nekos.fact()
    send(update,fact)

def urban(update, context):
    url= f'https://api.urbandictionary.com/v0/define?term={update.message.text}'
    request = requests.get(url)
    outputJ = json.loads(request.text)
    output = outputJ['definition']
    update.message.reply_text(output)

def google(update, context):
    term = filter(update)
    for a in search(term, tld="co.in", num=1, stop=1, pause=1.0):
        send(update,a)

def meme(update, context):
    sub = "memes"
    meme = Subreddit(sub)
    meme.get_random()
    memeT = meme.title
    memeP = meme.url
    sendImg(update,context,memeP)
    send(update,memeT)

def debuger(update, context):
    update.message.reply_text(f"You have appended ```{filter(update)}```\n to the debugger message")

def AI(update: Update, context: CallbackContext):
    message = update.message.text
    url = requests.get('http://api.brainshop.ai/get?bid=BRAINID&key=BRAINKEY&uid=[666]&msg='+message)
    decode = json.loads(url.text)
    ai = decode['cnt']
    update.message.reply_text(ai)

def main():
    print('Started main function')
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    addCom(dp,'meme',meme)
    dp.add_handler(CommandHandler('neko',neko))
    dp.add_handler(CommandHandler('kitsune',kitsune))
    dp.add_handler(CommandHandler('cat',cat))
    dp.add_handler(CommandHandler('g',google))
    dp.add_handler(CommandHandler('fact',fact))
    dp.add_handler(CommandHandler('urban',urban))
    dp.add_handler(CommandHandler('debuger',debuger))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, AI))
    updater.start_polling()
    print('Connected to telegram !')
    updater.idle()

if __name__ == '__main__':
    main()
