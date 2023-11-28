from telegram.constants import ParseMode
from src.constants import markup_assistant

def assistant(bot, callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, f'*Ассистенты*\n Выберите чемпионат', reply_markup=markup_assistant, parse_mode=ParseMode.MARKDOWN)
