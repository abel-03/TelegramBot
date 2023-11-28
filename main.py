import telebot
from src.menu import menu
from src.bombardier import bombardier
from src.table import table
from src.assistant import assistant
from src.get_table import get_table
from src.get_bombardier import get_bombardier
from src.get_assistant import get_assistant

bot = telebot.TeleBot('YOUR-BOT-TOKEN')

@bot.message_handler(commands=['start', 'menu'])
def main(message):
    menu(bot, message.chat.id)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'table':
        table(bot, callback)
    elif callback.data == 'bombardier':
        bombardier(bot, callback)
    elif callback.data == 'assistant':
        assistant(bot, callback)
    elif callback.data == 'menu':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        menu(bot, callback.message.chat.id)
    elif callback.data == 'england':
        get_table(bot, callback, 'https://www.sports.ru/epl/table/', 'england')
    elif callback.data == 'germany':
        get_table(bot, callback, 'https://www.sports.ru/bundesliga/table/', 'germany')
    elif callback.data == 'italy':
        get_table(bot, callback, 'https://www.sports.ru/seria-a/table/', 'italy')
    elif callback.data == 'spain':
        get_table(bot, callback, 'https://www.sports.ru/la-liga/table/', 'spain')
    elif callback.data == 'france':
        get_table(bot, callback, 'https://www.sports.ru/ligue-1/table/', 'france')
    elif callback.data == 'USA':
        get_table(bot, callback, 'https://www.sports.ru/mls/table/', 'USA')
    elif callback.data == 'arabia':
        get_table(bot, callback, 'https://www.sports.ru/saudi-pro-league/table/', 'arabia')
    elif callback.data == 'england_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/epl/bombardiers/')
    elif callback.data == 'germany_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/bundesliga/bombardiers/')
    elif callback.data == 'italy_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/seria-a/bombardiers/')
    elif callback.data == 'spain_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/la-liga/bombardiers/')
    elif callback.data == 'france_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/ligue-1/bombardiers/')
    elif callback.data == 'USA_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/mls/bombardiers/')
    elif callback.data == 'arabia_bombardier':
        get_bombardier(bot, callback, 'https://www.sports.ru/saudi-pro-league/bombardiers/')
    elif callback.data == 'england_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/epl/bombardiers/?s=goal_passes')
    elif callback.data == 'germany_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/bundesliga/bombardiers/?s=goal_passes')
    elif callback.data == 'italy_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/seria-a/bombardiers/?s=goal_passes')
    elif callback.data == 'spain_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/la-liga/bombardiers/?s=goal_passes')
    elif callback.data == 'france_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/ligue-1/bombardiers/?s=goal_passes')
    elif callback.data == 'USA_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/mls/bombardiers/?s=goal_passes')
    elif callback.data == 'arabia_assistant':
        get_assistant(bot, callback, 'https://www.sports.ru/saudi-pro-league/bombardiers/?s=goal_passes')



bot.infinity_polling()