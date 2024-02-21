import re
from datetime import datetime

def sort_by_merge(l: list) -> list:
    if len(l) <= 1:
        return l
    else:
        return merge(sort_by_merge(l[:len(l)//2]), sort_by_merge(l[len(l)//2:]))


def merge(l1: list, l2: list) -> list:
    lall, i, j = [], 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lall.append(l1[i])
            i += 1
        else:
            lall.append(l2[j])
            j += 1

    lall += l1[i:]
    lall += l2[j:]
    return lall


# Открываем файл для чтения
with open('powermorning_sescdraft2.txt', 'r') as f:
    # Читаем все строки из файла
    lines = f.readlines()
    lns = [[0, 0, 0]]*2300
    for line in lines:
        date = re.search(r"\d{2}/\d{2}/\d{4}", line)
        a = re.search(r"зарядка будет|будет прогулка", line)
        b = re.search(r'(-?\d+)°', line)
        degrees = b.group()[:-1] if b else 'None'
        pwnbe = '1' if a else '0'
        if date and degrees != 'None':
            #print(pwnbe)
            date = re.search(r"\d{2}/\d{2}/\d{4}", line).group()
            start_date = datetime(2018, 1, 21)
            dates = list(map(int, date.split('/')))
            end_date = datetime(dates[2], dates[0], dates[1])
            delta = end_date - start_date
            m, d, y = date.split('/')
            lns[delta.days] = [d, m, y, pwnbe, degrees]

i = 0
while i < len(lns):
    if lns[i] == [0, 0, 0]:
        del lns[i]
    else:
        i += 1


with open('данные_для_модели.txt', 'w') as f:
    # Записываем данные в файл итеративно
    for i in lns:
        #print(i)
        #print((',').join(i))
        
        f.write(f"{(',').join(i)}\n")

print("Данные успешно добавлены в файл 'данные_для_модели.txt'")
