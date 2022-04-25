from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru'

def get_soup(url):
    '''Функция, возвращающая экземпляр soup'''
    r = requests.get(url)
    return BeautifulSoup(r.text, features="html.parser")

def get_jams_info():
    '''Функция, возвращающая информацию о пробках'''
    soup = get_soup(url)
    info = soup.find('div', {'class': 'traffic__rate-text'})

    try:
        if int(info.text) == 1:
            return f'Пробки в Москве оцениваются в {info.text} балл'
        elif 1 < int(info.text) < 5:
            return f'Пробки в Москве оцениваются в {info.text} балла'
        else:
            return f'Пробки в Москве оцениваются в {info.text} баллов'
    except:
        return 'Не удалось получить ответ от Яндекса, попробуйте еще раз'
