from bs4 import BeautifulSoup
import requests
import random

def get_soup(url):
    '''Функция, возвращающая экземпляр soup'''
    r = requests.get(url, headers = {'User-agent': 'Sunews 0.1'})
    return BeautifulSoup(r.text, features="html.parser")


def get_news(category):
    '''Функция, возвращающая заголовок и ссылку случайной новости.
    На вход принимает строку с именем категории'''

    try:
        url = f'https://ria.ru/{category}' # religion, science, culture
        soup = get_soup(url)

        # находим все теги с нужным классом
        spanlist = soup.find_all('span', {'class': 'cell-list-f__item-title'})

        # берем случайный тег
        span = spanlist[random.randrange(0, len(spanlist))]

        # из ближайшего родителя <a> выбранного тега вытаскиваем url 
        link = span.find_parent('a')['href']

        # возвращаем заголовок новости + ссылку на нее
        result = [span.text, link]
        return result
    except:
        return ['Не удалось получить данные, попробуйте еще раз', '']
