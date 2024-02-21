import requests
from bs4 import BeautifulSoup
#
# URL страницы, с которой вы хотите получить данные
url = 'https://weather.nsu.ru/?start=2018.02.01&end=2018.02.28&std=various#gzsxiuxxst'

# Отправляем GET-запрос на указанный URL
response = requests.get(url)

# Проверяем, успешно ли выполнен запрос
if response.status_code == 200:
    # Получаем HTML-код страницы
    html_code = response.text
    print(html_code)
    # Создаем объект BeautifulSoup для парсинга HTML-кода
    soup = BeautifulSoup(html_code, 'html.parser')
    
    # Находим все div элементы с заданными стилями
    div_elements = soup.find_all('div', style=lambda value: value and 'position:absolute' in value)
    
    # Получаем данные о температуре из высоты каждого div элемента
    temperature_data = [int(div['style'].split(';')[3].split(':')[1][:-2]) for div in div_elements]
    
    # Выводим полученные данные о температуре
    print("Temperature data:", temperature_data)
else:
    print("Failed to retrieve the webpage.")
