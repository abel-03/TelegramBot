import requests
from bs4 import BeautifulSoup
from src.constants import position, count_matches
from telebot import types


def get_table(bot, callback, url, country):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    table_block = soup.find('div', class_='stat mB6')

    clubs = []
    points = []
    matches = []

    for row in table_block.select('tbody tr'):
        club_name_element = row.select_one('.name-td a')
        club_name = club_name_element.text.strip()
        
        club_points_element = row.find_all('td')[-1]
        club_points = club_points_element.text.strip()

        matches_count_element = row.find_all('td')[2]
        matches_count = matches_count_element.text.strip()

        clubs.append(club_name)
        points.append(club_points)
        matches.append(matches_count)

    message = "Таблица:\n"
    for i in range(len(clubs)):
        message += f"{position[i]} {clubs[i]}: {points[i]} ({matches[i]}/{count_matches[country]})\n"

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Назад', callback_data='table')
    markup.row(button)
    

    bot.send_message(callback.message.chat.id, message, reply_markup=markup)