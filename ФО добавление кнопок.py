"""
import telebot
from telebot import types
from secret import ticket

bot = telebot.TeleBot(ticket)
#reply_markup=ReplyKeyboardRemove()
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Список класса")
    markup.add(btn)
    bot.send_message(message.chat.id,'Привет что ты хочешь?', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Список класса':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
bot.infinity_polling()
"""