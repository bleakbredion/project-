import sqlite3
from secret import datebaseway1
def add_room_info(name_list, room_type, room_number):
    name_list.append(room_type)
    name_list.append(room_number)


list_of_9_3 = ['Анчугов Андрей', 'Барнашев Алексей', 'Белкин Илья', 'Бирюкова Дарья', 'Галабурдина Вероника', 'Голубцова Ксения', 'Грингольц Матвей', 'Гришечкин Илья', 'Евграфов Егор', 'Ефимов Петр',\
               'Зяблов Ростислав', 'Ионов Алексей', 'Казаков Федор', 'Коваль Михаил', 'Лебедева Екатерина', 'Лучкина София', 'Мищенко Тимофей', 'Никитин Евгений', 'Никитина Оксана', 'Перепелкин Петр',\
                'Подчасова Екатерина', 'Просеков Климентий', 'Тумилевич Вероника', 'Фоменко Полина', 'Чайвургин Денис', 'Шуберт София', 'Яцук Полина']

eng_trans_name = ['Anchugov_Andrey', 'Barnashev_Alexey', 'Belkin_Ilya', 'Biryukova_Darya', 'Galaburdina_Veronika', 'Golubtsova_Kseniya', 'Gringolts_Matvey', 'Grishechkin_Ilya',\
                  'Evgrafov_Egor', 'Efimov_Petr', 'Zyablov_Rostislav', 'Ionov_Alexey', 'Kazakov_Fedor', 'Koval_Mikhail', 'Lebedeva_Ekaterina', 'Luchkina_Sofia',\
                  'Mishchenko_Timofey', 'Nikitin_Yevgeny', 'Nikitina_Oksana', 'Perepelkin_Petr', 'Podchasova_Ekaterina', 'Prosekov_Klimentiy', 'Tumilevich_Veronika', \
                  'Fomenko_Polina', 'Chaivurgin_Denis', 'Shubert_Sofia', 'Yatsuk_Polina']

rm305 = ['Зяблов Ростислав', 'Казаков Федор', '305m']
rm307 = ['Никитина Оксана', 'Галабурдина Вероника', '307m']
rm311 = ["Подчасова Екатерина", "Лебедева Екатерина", '311m']
rb311 = ["Шуберт София", "Лучкина София", "Бирюкова Дарья", '311b']
rm313 = ["Грингольц Матвей", "Мищенко Тимофей", '313m']
rb313 = ["Чайвургин Денис", "Перепелкин Петр", "Анчугов Андрей", "Евграфов Егор", '313b']
rm314 = ["Коваль Михаил", "Ефимов Петр", '314m']
rb314 = ["Ионов Алексей", "Никитин Евгений", "Просеков Климентий", 'Белкин Илья', '314b']
rb316 = ["Барнашев Алексей", "Гришечкин Илья", '316b']
rm415 = ["Тумилевич Вероника", "Яцук Полина", '415m']
rb415 = ["Фоменко Полина", "Голубцова Ксения", '415b']

blocks = [rm305, rm307, rm311, rb311, rm313, rb313, rm314, rb314, rb316, rm415, rb415]


"""conn = sqlite3.connect('datebaseway1')

cursor = conn.cursor()



all_rooms = ['rm305', 'rm307', 'rm311', 'rb311', 'rm313', 'rb313', 'rm314', 'rb314', 'rb316','rm413', 'rm415', 'rb415']
all_inf = []
for room in all_rooms:
    rooom = globals()[room]
    #print(type(rooom))
    #print(rooom)
    room_type = 'small' if room[1].lower() == 'm' else 'large'
    #print(room_type)
    room_number = room[2:]
    rooom.extend([room_type, room_number])
    all_inf.append(rooom)
students = [tuple(simple_inf for people in room for simple_inf in people) for room in all_inf]

students = [('Зяблов Ростислав', 'Zyablov_Rostislav', 305, 'small'), ('Казаков Федор', 'Kazakov_Fedor', 305, 'small')]
"""
#cursor.execute("""
"""CREATE TABLE IF NOT EXISTE class9_3 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT PRIMARY KEY,
        english_translit_of_name PRIMARY KEY TEXT
        room_type TEXT CHECK(room_size IN ('small', 'large'))
        room_number INTEGER
        
    )"""
#""")
"""cursor.executemany('INSERT INTO class9_3 (name, english_translite_of_name,room_number, room_type) VALUES (?, ?, ?, ?), students')
conn.commit
conn.close
"""

"""conn = sqlite3.connect(datebaseway1)
cursor = conn.cursor()

columns = ['Day DATE DEFAULT CURRENT_DATE'] + [f'{i} TEXT CHECK({i} IN ("Come", "Ill", "Gone", "Don`t come"))' for i in eng_trans_name]

create_table_query = f'CREATE TABLE attendance_log ({", ".join(columns)});'

                    #['satust TEXT CHECK(status IN ("Come", "Ill", "Gone", "Don`t come"))']\
cursor.execute(create_table_query)

# Сохраните изменения и закройте соединение
conn.commit()
conn.close()"""



"""conn = sqlite3.connect(datebaseway1)
cursor = conn.cursor()



cursor.execute("INSERT INTO attendance_log(Anchugov_Andrey)\n VALUES ('Come');")


conn.commit()
conn.close()"""

"""conn = sqlite3.connect(datebaseway1)
cursor = conn.cursor()

columns = ['Day DATE DEFAULT CURRENT_DATE'] + [f'{i} TEXT CHECK({i} IN ("Come", "Ill", "Gone", "Don`t come", "Cleaning"))' for i in eng_trans_name]

create_table_query = f'CREATE TABLE attendance_log ({", ".join(columns)});'

                    #['status TEXT CHECK(status IN ("Come", "Ill", "Gone", "Don`t come"))']\
cursor.execute(create_table_query)

# Сохраните изменения и закройте соединение
conn.commit()
conn.close()"""


"""conn = sqlite3.connect(datebaseway1)
cursor = conn.cursor()

columns = ['Variable STRING', 'Value STRING']

create_table_query = f'CREATE TABLE glob_var_and_val ({", ".join(columns)});'

cursor.execute(create_table_query)

conn.commit()
conn.close()"""

"""conn = sqlite3.connect(datebaseway1)
cursor = conn.cursor()
#f'SELECT * FROM glob_var_and_val ', nd_fdback=True

columns = ['Variable STRING', 'Value STRING']

create_table_query = f'CREATE TABLE glob_var_and_val ({", ".join(columns)});'

cursor.execute(create_table_query)

conn.commit()
conn.close()"""

import sqlite3
"""
def add_ndpwmn():
    conn = sqlite3.connect(datebaseway1)
    cursor = conn.cursor()

    # Проверяем, есть ли уже запись для переменной ndpwmn
    check_query = 'SELECT * FROM glob_var_and_val WHERE Variable = "ndpwmn";'
    cursor.execute(check_query)
    existing_record = cursor.fetchone()

    if not existing_record:
        # Если записи нет, добавляем новую
        insert_query = 'INSERT INTO glob_var_and_val (Variable, Value) VALUES ("ndpwmn", "False");'
        cursor.execute(insert_query)
        conn.commit()

    conn.close()

# Вызываем функцию для добавления переменной ndpwmn
add_ndpwmn()
""""""
def update_ndpwmn(value):
    conn = sqlite3.connect(datebaseway1)
    cursor = conn.cursor()

    # Обновляем значение переменной ndpwmn
    update_query = f'UPDATE glob_var_and_val SET Value = "{[value, "25.02.2024"]}" WHERE Variable = "ndpwmn";'
    cursor.execute(update_query)
    conn.commit()

    conn.close()

# Пример использования: обновление на True
update_ndpwmn("False")
"""
"""
import sqlite3

def get_variable_value(variable_name):
    conn = sqlite3.connect(datebaseway1)
    cursor = conn.cursor()

    # Выбираем значение переменной по её имени
    select_query = f'SELECT Value FROM glob_var_and_val WHERE Variable = "{variable_name}";'
    cursor.execute(select_query)
    result = cursor.fetchone()

    conn.close()

    # Возвращаем значение, если оно найдено
    #return result[0] if result else None
    return result

# Пример использования: получение значения переменной ndpwmn
ndpwmn_value = get_variable_value("ndpwmn")
print(ndpwmn_value)
"""