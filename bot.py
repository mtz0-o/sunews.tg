import telebot
from telebot import types
import traffic_jams
import ruble
import news
import weather

TOKEN = '5227729795:AAFcAa9Eg23Ham-ohXxoo7SDTDr2HPqhUNM'

# записываем инстанс бота в переменную
bot = telebot.TeleBot(TOKEN)

# функция создания клавиатуры, на входе - массив названий кнопок
def create_markup(btn_names):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in btn_names:
        markup.add(types.KeyboardButton(name))
    return markup

# создаем метод приветствия с декоратором, обрабатывающим запрос /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_mes = 'Привет! Я информационный бот Sunews. Что вы хотите узнать?'
    markup = create_markup(['Курс рубля', 'Погода в Москве', 'Пробки в Москве', 'Новости'])

    # отправляем собеседнику приветствие и отдаем ему клавиатуру
    bot.send_message(chat_id=message.chat.id, text=welcome_mes, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    '''Единая функция для обработки всех текстовых сообщений'''
    if message.text == 'Пробки в Москве':
        bot.send_message(message.chat.id, text=traffic_jams.get_jams_info())

    if message.text == 'Курс рубля':
        markup = create_markup(['Фунт стерлингов Соединенного королевства', 'Доллар США', 'Евро', 'Назад'])
        mes = 'Выберите валюту'
        bot.send_message(chat_id=message.chat.id, text=mes, reply_markup=markup)

    if message.text == 'Евро':
        bot.send_message(chat_id=message.chat.id, text=ruble.get_value('EUR'))
    if message.text == 'Фунт стерлингов Соединенного королевства':
        bot.send_message(chat_id=message.chat.id, text=ruble.get_value('GBP'))
    if message.text == 'Доллар США':
        bot.send_message(chat_id=message.chat.id, text=ruble.get_value('USD'))

    if message.text == 'Новости':
        markup = create_markup(['Религия', 'Наука', 'Культура', 'Назад'])
        mes = 'Выберите категорию'
        bot.send_message(chat_id=message.chat.id, text=mes, reply_markup=markup)

    if message.text == 'Религия':
        ans = news.get_news('religion')
        res = give_news(ans)
        bot.send_message(chat_id=message.chat.id, text=res)
    if message.text == 'Наука':
        ans = news.get_news('science')
        res = give_news(ans)
        bot.send_message(chat_id=message.chat.id, text=res)
    if message.text == 'Культура':
        ans = news.get_news('culture')
        res = give_news(ans)
        bot.send_message(chat_id=message.chat.id, text=res)
        
    if message.text == 'Назад':
        send_welcome(message)

    if message.text == 'Погода в Москве':
        markup = create_markup(['Сегодня', 'Завтра', 'Послезавтра', 'Назад'])
        mes = 'Какой день вас интересует?'
        bot.send_message(chat_id=message.chat.id, text=mes, reply_markup=markup)

    if message.text == 'Сегодня':
        bot.send_message(chat_id=message.chat.id, text=weather.get_weather('today'))
    if message.text == 'Завтра':
        bot.send_message(chat_id=message.chat.id, text=weather.get_weather('tomorrow'))
    if message.text == 'Послезавтра':
        bot.send_message(chat_id=message.chat.id, text=weather.get_weather('a_tomorrow'))    


# дополнительная функция для вывода новостей
# ради сокращения кода
def give_news(answer):
    title = answer[0]
    link = answer[1]
    res = f'{title}\n{link}'
    return res

print(ruble.get_value('USD'))

bot.polling(none_stop=True)

