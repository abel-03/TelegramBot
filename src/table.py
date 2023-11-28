from telegram.constants import ParseMode
from src.constants import markup_table

def table(bot, callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, f'*Таблица*\nВыберите чемпионат', reply_markup=markup_table, parse_mode=ParseMode.MARKDOWN)
    