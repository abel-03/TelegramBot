import requests
from bs4 import BeautifulSoup
from src.constants import position
from telebot import types


def get_bombardier(bot, callback, url):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    table_block = soup.find('div', class_='stat mB6')

    clubs = []
    points = []
    top = []

    for row in table_block.select('tbody tr'):
        club_name_element = row.select_one('.name-td a')
        club_name = club_name_element.text.strip() 

        club_points_element = row.find_all('td')[4]
        club_points = club_points_element.text.strip()

        top_elements = row.find_all('td')[0]
        top_elem = top_elements.text.strip()

        clubs.append(club_name)
        points.append(club_points)
        top.append(top_elem)

    message = "Бомбардиры:\n"
    for i in range(20):
        message += f"{position[int(top[i]) - 1]} {clubs[i]}: {points[i]}\n"

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Назад', callback_data='bombardier')
    markup.row(button)
    

    bot.send_message(callback.message.chat.id, message, reply_markup=markup)