from telegram.constants import ParseMode
from src.constants import markup_bombardier

def bombardier(bot, callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, f'*Бомбардиры*\n Выберите чемпионат', reply_markup=markup_bombardier, parse_mode=ParseMode.MARKDOWN)
