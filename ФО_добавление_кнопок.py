"""
bot = telebot.TeleBot(ticket)
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
import sqlite3
import telebot
from telebot import types
from secret import datebaseway1, access_token, mychatid, ticket, group9_3sportchatid, group9_3chatid
from datetime import datetime, timedelta, date, time
import time
from ФО_database import list_of_9_3, eng_trans_name, blocks
import requests
import re

def morning() -> str:
    l = [f"/{eng_trans_name[i]} / {list_of_9_3[i]}\n" for i in range(len(eng_trans_name))]
    snd_msgg = ' '.join(l)
    return snd_msgg


def morning_cond() -> str:
    atten = req_to_db(f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()).split()[0]}"', nd_fdback=True)
    if atten != None:
        #l = [f"/{eng_trans_name[i]} / {list_of_9_3[i]}\n{' '*(4+10+len(eng_trans_name[i])+len(list_of_9_3[i]))}<b>{atten[i+1]}</b>\n" if atten[i+1] is not None else f"/{eng_trans_name[i]} / {list_of_9_3[i]}\n" for i in range(len(eng_trans_name))]
        l = [f"/{eng_trans_name[i]} / {list_of_9_3[i]} - <b>{atten[i+1]}</b>\n" if atten[i+1] is not None else f"/{eng_trans_name[i]} / {list_of_9_3[i]}\n" for i in range(len(eng_trans_name))]
        snd_mes = ' '.join(l)
        #print(snd_msgg)
    else:
        snd_mes = morning()
    return snd_mes


def morning_by_blocks() -> str:
    l = [f"{room[-1]}\n" + '\n'.join(f"/{eng_trans_name[list_of_9_3.index(peop)]} / {peop}" for peop in room[:-1]) for room in blocks]
    snd_mes = '\n'.join(l)
    return snd_mes


def morning_by_blocks_cond() -> str:
    atten = req_to_db(f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()).split()[0]}"', nd_fdback=True)
    #print(atten)
    if atten != None:
        l = [f"{room[-1]}\n" + '\n'.join(f"/{eng_trans_name[list_of_9_3.index(peop)]} / {peop} - <b>{atten[list_of_9_3.index(peop)+1]}</b>" if atten[list_of_9_3.index(peop)+1] is not None else \
                                         f"/{eng_trans_name[list_of_9_3.index(peop)]} / {peop}" for peop in room[:-1]) for room in blocks]
        snd_mes = '\n'.join(l)
    else:
        snd_mes = morning_by_blocks()
    return snd_mes

def req_to_db(request="", nd_fdback=False):
    conn = sqlite3.connect(datebaseway1)
    cursor = conn.cursor()
    cursor.execute(request)
    result = None
    if nd_fdback:
        result = cursor.fetchone()
        #print(result)
    conn.commit()
    conn.close()
    return result



"""x = (req_to_db(request=f'SELECT Value FROM glob_var_and_val WHERE Variable = "ndpwmn";', nd_fdback=True)[0]).split(", ")
x1, x2 = x[0][2:len(x[0])-1], x[1][1:len(x[1])-2]
print(x1, x2)
"""
#req_to_db(request=f'SELECT Value FROM glob_var_and_val WHERE Variable = "{"ndpwmn"}";', nd_fdback=True)
#   print(list(req_to_db(request=f'SELECT Value FROM glob_var_and_val WHERE Variable = "{"ndpwmn"}";', nd_fdback=True))[0].split(","))

def make_cont(cond: str):
    atten = None
    i = 0
    while atten == None:
        atten = req_to_db(f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()-timedelta(days=i)).split()[0]}"', nd_fdback=True)
        i+=1
    forslash = '\n'
    try:
        mes = f"({atten.count(cond)}):{forslash}{''.join(['/' + eng_trans_name[name-1] + ' / ' + list_of_9_3[name-1] + forslash for name in [exp for exp in range(len(atten)) if atten[exp] == cond]])}"
    except AttributeError as e:
        mes = f"({atten.count(cond)}):{forslash}{''.join(['/' + eng_trans_name[name-1] + ' / ' + list_of_9_3[name-1] + forslash for name in [exp for exp in range(len(atten)) if atten[exp] == cond]])}"
    return mes


def vis_atten_td() -> str:
    descript = ['Вот кто сегодня пришел', 'Вот кто болеет', 'Уехал(а)', 'Убираются', 'Не пришли']
    #mes = descript[0] + make_cont(cond='Gone')
    mes = ''.join([descript[i] + make_cont(cond=['Come', 'Ill', 'Gone', 'Cleaning', 'Don`t come'][i]) for i in range(5)])
    #print(type(mes))
    #mes = f"{forslash}{''.join(['/' + eng_trans_name[name-1] + ' / ' + list_of_9_3[name-1] + forslash for name in [exp for exp in range(len(atten)) if atten[exp] == 'Come']])}"
    return mes


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


def pwmbe() -> [int, str, str]:
    posts = get_posts(get_group_id('powermorning_sesc', access_token), access_token, 1)
    datelikepwm = datetime.now().strftime("%d.%m")
    #datelikepwm = "19.01"
    pst = posts[0]
    try:
        re.search(datelikepwm, pst).group()
        """
        try:
            re.search("не будет", pst).group()
            #print("не будет")
            ans = 0
        except AttributeError as e:
            #print("будет")
            ans = 1
        """
        x = pst.find("будет")
        if pst.find("не", x-3, x)+1:
            ans = 0
        else:
            ans = 1
    except AttributeError as e:
        ans = -1
    return [ans, pst, datelikepwm]


def wait_for_time(need_ask=True, lrgtime=[6, 42], rrgtime=[7, 45]) -> int:
    H, M, S = map(int, datetime.now().strftime("%H:%M:%S").split(":"))
    HMinM = H*60+M
    l, r = lrgtime[0]*60+lrgtime[1], rrgtime[0]*60+rrgtime[1]
    if not need_ask:
        return -1
    elif HMinM < l or HMinM > r:
        waitingtime = (1440*int(not bool(datetime.now().weekday()-5)) + (l+1440-HMinM)%1440)*60-S
        time.sleep(waitingtime)
        H, M = map(int, datetime.now().strftime("%H:%M").split(":"))
        HMinM = H*60+M
    return (abs(r-HMinM)+(r-HMinM))//2

bot = telebot.TeleBot(ticket)

def pwmbe_in_chat(wttm = False):
    #req_to_db()
    if wttm:
        wait_for_time()
    x = (req_to_db(request=f'SELECT Value FROM glob_var_and_val WHERE Variable = "ndpwmn";', nd_fdback=True)[0]).split(", ")
    x1, x2 = x[0][2:len(x[0])-1], x[1][1:len(x[1])-2]
    if x2 != datetime.now().strftime("%d.%m.%Y"):
        while not (pwmbe()[0]+1):
            print("Жду минуту...")
            time.sleep(60)
        itbe, pst, dt = pwmbe()
        if itbe:
            print(pst, 'Зарядка будет')
            pwmrbe = 'Зарядка будет'
        else:
            print(pst, 'Зарядки не будет')
            pwmrbe = 'Зарядки не будет'

        #bot.send_message(chat_id=mychatid, text=f"Сегодня {dt} и <b>{pwmrbe}</b>", parse_mode="HTML")
        ch_id_send = group9_3chatid
        #ch_id_send = mychatid
        bot.send_message(chat_id=ch_id_send, text=f"Сегодня {dt} и <b>{pwmrbe}</b>", parse_mode="HTML", message_thread_id=ch_id_send)
        #bot.send_message(chat_id=ch_id_send, text=f"Сегодня {dt} и <b>{pwmrbe}</b>", parse_mode="HTML")
        if itbe:
            bot.send_message(chat_id=ch_id_send, text="Сбор как обычно в 32-е минуты", disable_notification=True, message_thread_id=ch_id_send)
            #bot.send_message(chat_id=ch_id_send, text="Сбор как обычно в 32-е минуты", disable_notification=True)
        req_to_db(request=f'UPDATE glob_var_and_val SET Value = "{["False", datetime.now().strftime("%d.%m.%Y")]}" WHERE Variable = "ndpwmn";')
    else:
        print("Today it`s already be")




def a():
    bot.send_message(chat_id=group9_3chatid, text="Сбор как обычно в 32-е минуты", disable_notification=True, message_thread_id=group9_3sportchatid)


#a = wait_time_for(lrgtime=[21, 48], rrgtime=[21, 48])
#print(a)

#print(req_to_db(f'SELECT * FROM attendance_log WHERE Day = "{str(datetime.now()).split()[0]}"', nd_fdback=True))
#morning_cond()
#morning_by_blocks_cond()

"""group_domain = 'powermorning_sesc'
count = 1
filename = 'powermorning_sescdraft.txt'
group_id = get_group_id(group_domain, access_token)
posts = get_posts(group_id, access_token, count)"""
#save_posts_to_file(posts, filename)
#print(posts)
#print(pwmbe())

#pwmbe_in_chat(wttm=False)
#a()


