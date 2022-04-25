from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru'

def get_soup(url):
    '''Функция, возвращающая экземпляр soup'''
    r = requests.get(url)
    return BeautifulSoup(r.text, features="html.parser")

def get_weather(day):
    '''Функция, возвращающая температуру днем. На вход принимает строку:
        'today' - сегодня,
        'tomorrow' - завтра,
        'a_tomorrow' - послезавтра
    '''
    url = 'https://weather.rambler.ru/v-moskve/'

    if day == 'today':
        tag = 'div'
        classname = '_1HBR _3mFL'
        index = 0
        day_mes = 'Сегодня'
    elif day == 'tomorrow':
        tag = 'span'
        classname = 'bLo8'
        index = 0
        day_mes = 'Завтра'
    elif day == 'a_tomorrow':
        tag = 'span'
        classname = 'bLo8'
        index = 1
        day_mes = 'Послезавтра'


    try:
        soup = get_soup(url)
        temp = soup.find_all(tag, {'class': classname})
        return f'{day_mes} в Москве {temp[index].text}'
    except:
        return 'Не удалось получить данные, попробуйте снова'