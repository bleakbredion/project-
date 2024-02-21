#from telegram import ParseMode #pip install python-telegram-bot
#from telegram.ext import Updater, MessageHandler, Filters, Defaults
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
import sqlite3
from ФО_database import list_of_9_3, eng_trans_name, rm305, rm307, rm311, rb311, rm313, rb313, rm314, rb314, rb316, rb415, rm415
from datetime import datetime, date, time, timedelta
import time
from secret import ticket, datebaseway1, mychatid
from ФО_добавление_кнопок import morning, morning_cond, morning_by_blocks,morning_by_blocks_cond, req_to_db, vis_atten_td, pwmbe_in_chat
import threading

lastname = 'None'
condition = True
pwmrbe = None
bot = telebot.TeleBot(ticket)

@bot.message_handler(commands=['get_prev_message'])
def get_prev_message(message):
    chat_id = message.chat.id
    user_id_to_check = message.from_user.id

    try:
        #print("reached to 20 string")
        updates = bot.get_updates(limit=3, timeout=1, allowed_updates=["message"])
        #print("reached to 22 string")

        if updates:
            user_messages = [upd.message for upd in updates if upd.message.chat.id == chat_id and upd.message.from_user.id == user_id_to_check]

            if len(user_messages) >= 2:
                prev_message = user_messages[-2]
                bot.send_message(chat_id, f"Текст предпоследнего сообщения от пользователя: {prev_message.text}")
            else:
                bot.send_message(chat_id, "Недостаточно сообщений от пользователя для получения предпоследнего.")
    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка: {e}")


@bot.message_handler(commands=['start'])
def class_list(message):
    global lastname  # Добавил global
    #bot.send_message(message.chat.id, text=f"до этого ты говорил о нем/неё {lastname}")
    snd = morning()
    bot.send_message(message.chat.id, text=snd, reply_markup=ReplyKeyboardRemove())


@bot.message_handler(commands=eng_trans_name)
def name_func(message):
    global lastname
    lastname = message.text[1:]
    #print(lastname)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Пришел/Пришла')
    btn2 = types.KeyboardButton('Болеет')
    btn3 = types.KeyboardButton('Уехал(а)')
    btn4 = types.KeyboardButton('Не был(а)')
    btn5 = types.KeyboardButton('Убирается')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    #bot.send_message(message.chat.id, text=f"{lastname} ты о нём/ней?")
    bot.send_message(message.chat.id, text='Что с ним/ней произошло?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def executing_commands(message):
    global lastname, condition
    dick = {'Пришел/Пришла': 'Come', 'Болеет': 'Ill', 'Уехал(а)': 'Gone', 'Не был(а)': 'Don`t come', 'Убирается': 'Cleaning'}
    if message.text in ['Пришел/Пришла', 'Болеет', 'Уехал(а)', 'Не был(а)', 'Убирается']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список класса")
        #btn4 = types.KeyboardButton("Список класса with cond")
        btn2 = types.KeyboardButton("Список класса(по блокам)")
        btn3 = types.KeyboardButton("Журнал посещения")
        btn5 = types.KeyboardButton("Настройки")
        markup.add(btn1, btn2, btn3, btn5)
        req = f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()).split()[0]}"'
        if req_to_db(req, nd_fdback=True) != None:
            req = f'UPDATE attendance_log\nSET "{lastname}"="{dick[message.text]}"\nWHERE "Day" = "{str(datetime.now()).split()[0]}"'
        else:
            req = f"INSERT INTO attendance_log({lastname}, Day)\n VALUES ('{dick[message.text]}', '{str(datetime.now()).split()[0]}');"
        #print(req)
        req_to_db(req)
        bot.send_message(message.chat.id, text=f'Записал))) ({lastname})', reply_markup=markup)
    elif message.text == 'Список класса':
        snd = morning_cond() if condition else morning()
        bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
    #elif message.text == 'Список класса with cond':
    #   snd = morning_cond()
    #   bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
    elif message.text == 'Список класса(по блокам)':
        snd = morning_by_blocks_cond() if condition else morning_by_blocks()
        bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
    elif message.text == 'Журнал посещения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сегодня')
        #btn2 = types.KeyboardButton('За определенный')
        #btn3 = types.KeyboardButton('Назад')
        markup.add(btn1)
        #message_id = message.message_id
        bot.send_message(message.chat.id, text='За какой срок?', reply_markup=markup)
    elif message.text == 'Сегодня':
        snd = vis_atten_td()
        #print(type(snd))
        #print(snd)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список класса")
        btn2 = types.KeyboardButton("Список класса(по блокам)")
        btn3 = types.KeyboardButton("Журнал посещения")
        btn4 = types.KeyboardButton("Настройки")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=snd, reply_markup=markup)
    elif message.text == 'Настройки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВКЛ")
        btn2 = types.KeyboardButton("ВЫКЛ")
        markup.add(btn1, btn2)
        bot.send_message(text='conditions', chat_id=message.chat.id, reply_markup=markup)
    elif message.text == 'ВКЛ' or message.text == 'ВЫКЛ':
        condition = {'ВКЛ': True, 'ВЫКЛ': False}[message.text]
        snd = morning_cond() if condition else morning()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список класса")
        btn2 = types.KeyboardButton("Список класса(по блокам)")
        btn3 = types.KeyboardButton("Журнал посещения")
        btn4 = types.KeyboardButton("Настройки")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=snd, reply_markup=markup, parse_mode="HTML")


def run_bot():
    bot.polling(none_stop=True, interval=0)

thread2 = threading.Thread(target=pwmbe_in_chat(wttm=True))
thread1 = threading.Thread(target=run_bot())
#thread2 = threading.Thread(target=pwmbe_in_chat(), args=[False])

thread2.start()
thread1.start()

#pwmbe_in_chat(wttm=False)

"""
@bot.message_handler(commands=['get_prev_message'])
def get_prev_message(message):
    if message.chat.id == mychatid:
        chat_id = message.chat.id
        user_id_to_check = message.from_user.id

        try:
            #print("reached to 20 string")
            updates = bot.get_updates(limit=3, timeout=1, allowed_updates=["message"])
            #print("reached to 22 string")

            if updates:
                user_messages = [upd.message for upd in updates if upd.message.chat.id == chat_id and upd.message.from_user.id == user_id_to_check]

                if len(user_messages) >= 2:
                    prev_message = user_messages[-2]
                    bot.send_message(chat_id, f"Текст предпоследнего сообщения от пользователя: {prev_message.text}")
                else:
                    bot.send_message(chat_id, "Недостаточно сообщений от пользователя для получения предпоследнего.")
        except Exception as e:
            bot.send_message(chat_id, f"Произошла ошибка: {e}")
    else:
        print(f"Пришло сообшения от {message.chat.id}")


@bot.message_handler(commands=['start'])
def class_list(message):
    if message.chat.id == mychatid:
        global lastname  # Добавил global
        #bot.send_message(message.chat.id, text=f"до этого ты говорил о нем/неё {lastname}")
        snd = morning()
        bot.send_message(message.chat.id, text=snd, reply_markup=ReplyKeyboardRemove())
    else:
        print(f"Пришло сообшения от {message.chat.id}")


@bot.message_handler(commands=eng_trans_name)
def name_func(message):
    if message.chat.id == mychatid:
        global lastname
        lastname = message.text[1:]
        #print(lastname)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пришел/Пришла')
        btn2 = types.KeyboardButton('Болеет')
        btn3 = types.KeyboardButton('Уехал(а)')
        btn4 = types.KeyboardButton('Не был(а)')
        btn5 = types.KeyboardButton('Убирается')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        #bot.send_message(message.chat.id, text=f"{lastname} ты о нём/ней?")
        bot.send_message(message.chat.id, text='Что с ним/ней произошло?', reply_markup=markup)
    else:
        print(f"Пришло сообшения от {message.chat.id}")



@bot.message_handler(content_types=['text'])
def executing_commands(message):
    if message.chat.id == mychatid:
        global lastname, condition
        dick = {'Пришел/Пришла': 'Come', 'Болеет': 'Ill', 'Уехал(а)': 'Gone', 'Не был(а)': 'Don`t come', 'Убирается': 'Cleaning'}
        if message.text in ['Пришел/Пришла', 'Болеет', 'Уехал(а)', 'Не был(а)', 'Убирается']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Список класса")
            #btn4 = types.KeyboardButton("Список класса with cond")
            btn2 = types.KeyboardButton("Список класса(по блокам)")
            btn3 = types.KeyboardButton("Журнал посещения")
            btn5 = types.KeyboardButton("Настройки")
            markup.add(btn1, btn2, btn3, btn5)
            req = f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()).split()[0]}"'
            if req_to_db(req, nd_fdback=True) != None:
                req = f'UPDATE attendance_log\nSET "{lastname}"="{dick[message.text]}"\nWHERE "Day" = "{str(datetime.now()).split()[0]}"'
            else:
                req = f"INSERT INTO attendance_log({lastname}, Day)\n VALUES ('{dick[message.text]}', '{str(datetime.now()).split()[0]}');"
            #print(req)
            req_to_db(req)
            bot.send_message(message.chat.id, text=f'Записал))) ({lastname})', reply_markup=markup)
        elif message.text == 'Список класса':
            snd = morning_cond() if condition else morning()
            bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
        #elif message.text == 'Список класса with cond':
        #   snd = morning_cond()
        #   bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
        elif message.text == 'Список класса(по блокам)':
            snd = morning_by_blocks_cond() if condition else morning_by_blocks()
            bot.send_message(message.chat.id, text=snd, parse_mode="HTML")
        elif message.text == 'Журнал посещения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Сегодня')
            #btn2 = types.KeyboardButton('За определенный')
            #btn3 = types.KeyboardButton('Назад')
            markup.add(btn1)
            #message_id = message.message_id
            bot.send_message(message.chat.id, text='За какой срок?', reply_markup=markup)
        elif message.text == 'Сегодня':
            snd = vis_atten_td()
            #print(type(snd))
            #print(snd)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Список класса")
            btn2 = types.KeyboardButton("Список класса(по блокам)")
            btn3 = types.KeyboardButton("Журнал посещения")
            btn4 = types.KeyboardButton("Настройки")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text=snd, reply_markup=markup)
        elif message.text == 'Настройки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("ВКЛ")
            btn2 = types.KeyboardButton("ВЫКЛ")
            markup.add(btn1, btn2)
            bot.send_message(text='conditions', chat_id=message.chat.id, reply_markup=markup)
        elif message.text == 'ВКЛ' or message.text == 'ВЫКЛ':
            condition = {'ВКЛ': True, 'ВЫКЛ': False}[message.text]
            snd = morning_cond() if condition else morning()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Список класса")
            btn2 = types.KeyboardButton("Список класса(по блокам)")
            btn3 = types.KeyboardButton("Журнал посещения")
            btn4 = types.KeyboardButton("Настройки")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text=snd, reply_markup=markup, parse_mode="HTML")
    else:
        print(f"Пришло сообшения от {message.chat.id}")
"""