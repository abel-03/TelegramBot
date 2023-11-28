from telegram.constants import ParseMode
from telebot import types


def menu(bot, chat_id):
    markup3 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Турнирная таблица', callback_data='table')
    button2 = types.InlineKeyboardButton('Список бомбардиров', callback_data='bombardier')
    button3 = types.InlineKeyboardButton('Список ассистентов', callback_data='assistant')
    markup3.row(button1)
    markup3.row(button2)
    markup3.row(button3)
    
    bot.send_message(chat_id, f'Привет!\nЧто тебя интересует?', reply_markup=markup3, parse_mode=ParseMode.MARKDOWN)
