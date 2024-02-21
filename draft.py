import csv
import time
# Открываем файл для чтения
with open('/home/rostislav/project ФО/29637.21.01.2018.19.02.2024.1.0.0.ru.utf8.00000000.csv', 'r') as file:
    # Создаем объект чтения CSV
    csv_reader = csv.reader(file, delimiter=';')
    
    # Пропускаем заголовок, если он есть
    #next(csv_reader)
    i=0
    # Читаем и выводим столбец
    for row in csv_reader:
        #time.sleep(0.005)
        print(row[0], row[11])
        print(i)
        i += 1
       