import telebot
import config
import tm_text
import messages
from random import seed
from random import randint

bot = telebot.TeleBot(config.TOKEN_TEST)
seed(1)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, tm_text.START_TEXT + '  Sorry, you my lord!')


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, tm_text.HELLO_WORLD + ' Oh i thinks this some bret for user! ' + message.text)


@bot.channel_post_handler(commands=['start'])
def start_message_channel(message):
    bot.send_message(message.chat.id, tm_text.START_TEXT)


@bot.channel_post_handler(content_types=['text'])
def sendToChannel2(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, tm_text.HELLO_WORLD + ' Oh i thinks this some bret for user! ' + message.text)
    if message.text == "Ну нахер":
        bot.send_message(message.chat.id, 'Падре куда же вы?')
    if message.text == "Где картинка?":
        bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/63/IMG_%28business%29.svg'
                                        '/1200px-IMG_%28business%29.svg.png')
    if message.text == "Где stik?":
        bot.send_sticker(message.chat.id, 'https://t.me/test12565/81')
    else:
        bot.send_photo(message.chat.id, messages.IMG[randint(0, 2)])


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling(none_stop=True)
