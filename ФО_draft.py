"""
<b>Это жирный текст</b>
<i>Это курсив</i>
<u>Это подчеркнутый текст</u>
<a href="http://www.example.com">Текст ссылки</a>
<code>Инлайн-код</code>
<blockquote>Это цитата</blockquote>
"""
"""import telebot
from secret import ticket
import logging

logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot(ticket)

@bot.message_handler(commands=['get_prev_message'])
def get_prev_message(message):
    chat_id = message.chat.id
    user_id_to_check = message.from_user.id

    try:
        logging.debug("Trying to get updates...")
        updates = bot.get_updates(limit=100, timeout=20, allowed_updates=["message"])
        logging.debug("Got updates successfully.")

        # Получаем последние 100 обновлений (вы можете увеличить или уменьшить этот лимит)

        if updates:
            # Если есть обновления, обрабатываем их
            user_messages = [upd.message for upd in updates if upd.message.chat.id == chat_id and upd.message.from_user.id == user_id_to_check]

            if len(user_messages) >= 2:
                prev_message = user_messages[-2]
                bot.send_message(chat_id, f"Текст предпоследнего сообщения от пользователя: {prev_message.text}")
            else:
                bot.send_message(chat_id, "Недостаточно сообщений от пользователя для получения предпоследнего.")
    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)


print('swehbaseb')"""


"""import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('D:\\SQLite Studio\\ФО_HIGDC.db')
cursor = conn.cursor()

# SQL-запрос для вставки данных
sql_query = '''
    INSERT INTO ВашаТаблица (title, author, price, amount)
    VALUES (?, ?, ?, ?);
'''

# Данные для вставки
data = [
    ('Белая гвардия', 'Булгаков М.А.', 540.50, 5),
    ('Идиот', 'Достоевский Ф.М', 460.00, 10),
    ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2),
]

# Выполнение запроса для каждой строки данных
for row in data:
    cursor.execute(sql_query, row)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
"""

"""
import telebot
from telebot import types
import schedule
import time
from datetime import datetime, timedelta
from secret import ticket
import threading

bot = telebot.TeleBot(ticket)

def mor_routine():
    pass

target_time = "06:59"

# Функция, которую будет выполнять бот
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускайте бота в отдельном потоке
def run_bot():
    bot.polling(none_stop=True)

# Запускайте цикл, проверяя текущий день недели
def run_scheduler():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        current_day = datetime.now().strftime("%A")

        if current_day != "Sunday" and current_time == target_time:
            # Если не воскресенье и текущее время соответствует желаемому времени
            scheduled_job()

            # Подождите до следующего дня
            tomorrow = datetime.now() + timedelta(days=1)
            next_execution_time = datetime.combine(tomorrow.date(), datetime.strptime(target_time, "%H:%M").time())
            sleep_duration = (next_execution_time - datetime.now()).total_seconds()
            time.sleep(sleep_duration)
        else:
            # Подождите некоторое время перед следующей проверкой
            time.sleep(60)

# Создайте и запустите потоки
bot_thread = threading.Thread(target=run_bot)
scheduler_thread = threading.Thread(target=run_scheduler)

bot_thread.start()
scheduler_thread.start()
"""
import requests
import time
from secret import access_token


def get_group_id(group_domain, access_token):
    base_url = 'https://api.vk.com/method/groups.getById'
    params = {
        'group_id': group_domain,
        'access_token': access_token,
        'v': '5.131'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Выводим ответ от API VK для отладки
    #print(data)
    # Проверка наличия ключа 'error' в ответе API
    if 'error' in data:
        print(f"Error: {data['error']['error_msg']}")
        # Можно добавить дополнительную обработку ошибок здесь
        return None

    # Проверка наличия ключа 'response' перед использованием
    if 'response' in data and data['response']:
        group_id = data['response'][0]['id']
        return group_id
    else:
        print('Error: Response does not contain the expected data.')
        return None

def get_posts(group_id, access_token, count=100):
    base_url = 'https://api.vk.com/method/wall.get'
    posts = []
    offset = 0
    while count > 0:
        params = {
            'owner_id': -group_id,
            'count': min(count, 100),
            'offset': offset,
            'access_token': access_token,
            'v': '5.131'
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'response' in data and 'items' in data['response']:
            items = data['response']['items']
            # Extract the text from posts and add them to the list
            posts.extend([post['text'].replace('\n', ' ') for post in items if post['text']])
            count -= len(items)
            offset += len(items)
        else:
            print('Error occurred while getting posts. Please try adjusting the recommended delay.')
            break

        # Insert a delay between requests to avoid exceeding API limitations
        time.sleep(0.35)  # Recommended delay in case of errors: 0.35 seconds

    return posts


def save_posts_to_file(posts, filename, append=False):
    mode = 'a' if append else 'w'
    with open(filename, mode, encoding='utf-8') as file:
        # Write the posts to the file, separating them with double line breaks
        file.write('\n\n'.join(posts) + '\n\n')


group_domain = 'powermorning_sesc'
count = 1
filename = 'powermorning_sescdraft.txt'
group_id = get_group_id(group_domain, access_token)
posts = get_posts(group_id, access_token, count)
#save_posts_to_file(posts, filename)
print(posts)