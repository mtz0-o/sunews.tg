from bs4 import BeautifulSoup
import requests

def get_soup(url):
    '''Функция, возвращающая экземпляр soup'''

    r = requests.get(url, headers = {'User-agent': 'Sunews 0.1'})
    return BeautifulSoup(r.text, features="html.parser")

# EUR, GBP, USD - значения строк currency
def get_value(currency):
    '''Функция, возвращающая курс рубля к currency'''

    soup = get_soup('https://www.banki.ru/products/currency/cb')
    try:
        tr = soup.find('tr', {'data-currency-code': currency})
        tds = tr.find_all('td')
        return f'1 RUB = {tds[-2].text} {currency}'
    except:
        return 'Не удалось получить ответ от banki.ru, попробуйте еще раз'