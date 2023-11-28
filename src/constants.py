from telebot import types

markup_table = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Чемпионат Англии 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='england')
button2 = types.InlineKeyboardButton('Чемпионат Германии 🇩🇪', callback_data='germany')
button3 = types.InlineKeyboardButton('Чемпионат Италии 🇮🇹', callback_data='italy')
button4 = types.InlineKeyboardButton('Чемпионат Испании 🇪🇸', callback_data='spain')
button5 = types.InlineKeyboardButton('Чемпионат Франции  🇫🇷', callback_data='france')
button6 = types.InlineKeyboardButton('Чемпионат США 🇺🇸', callback_data='USA')
button7 = types.InlineKeyboardButton('Чемпионат Саудовской Аравии 🇸🇦', callback_data='arabia')
button8 = types.InlineKeyboardButton('Назад', callback_data='menu')

markup_table.row(button1)
markup_table.row(button2)
markup_table.row(button3)
markup_table.row(button4)
markup_table.row(button5)
markup_table.row(button6)
markup_table.row(button7)
markup_table.row(button8)


position = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣', '6️⃣', '7️⃣' , '8️⃣', '9️⃣', '🔟', 
            '1️⃣1️⃣', '1️⃣2️⃣', '1️⃣3️⃣', '1️⃣4️⃣', '1️⃣5️⃣', '1️⃣6️⃣', '1️⃣7️⃣', '1️⃣8️⃣', '1️⃣9️⃣', '2️⃣0️⃣']

markup_bombardier = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Чемпионат Англии 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='england_bombardier')
button2 = types.InlineKeyboardButton('Чемпионат Германии 🇩🇪', callback_data='germany_bombardier')
button3 = types.InlineKeyboardButton('Чемпионат Италии 🇮🇹', callback_data='italy_bombardier')
button4 = types.InlineKeyboardButton('Чемпионат Испании 🇪🇸', callback_data='spain_bombardier')
button5 = types.InlineKeyboardButton('Чемпионат Франции  🇫🇷', callback_data='france_bombardier')
button6 = types.InlineKeyboardButton('Чемпионат США 🇺🇸', callback_data='USA_bombardier')
button7 = types.InlineKeyboardButton('Чемпионат Саудовской Аравии 🇸🇦', callback_data='arabia_bombardier')
button8 = types.InlineKeyboardButton('Назад', callback_data='menu')

markup_bombardier.row(button1)
markup_bombardier.row(button2)
markup_bombardier.row(button3)
markup_bombardier.row(button4)
markup_bombardier.row(button5)
markup_bombardier.row(button6)
markup_bombardier.row(button7)
markup_bombardier.row(button8)


markup_assistant = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Чемпионат Англии 🏴󠁧󠁢󠁥󠁮󠁧󠁿', callback_data='england_assistant')
button2 = types.InlineKeyboardButton('Чемпионат Германии 🇩🇪', callback_data='germany_assistant')
button3 = types.InlineKeyboardButton('Чемпионат Италии 🇮🇹', callback_data='italy_assistant')
button4 = types.InlineKeyboardButton('Чемпионат Испании 🇪🇸', callback_data='spain_assistant')
button5 = types.InlineKeyboardButton('Чемпионат Франции  🇫🇷', callback_data='france_assistant')
button6 = types.InlineKeyboardButton('Чемпионат США 🇺🇸', callback_data='USA_assistant')
button7 = types.InlineKeyboardButton('Чемпионат Саудовской Аравии 🇸🇦', callback_data='arabia_assistant')
button8 = types.InlineKeyboardButton('Назад', callback_data='menu')

markup_assistant.row(button1)
markup_assistant.row(button2)
markup_assistant.row(button3)
markup_assistant.row(button4)
markup_assistant.row(button5)
markup_assistant.row(button6)
markup_assistant.row(button7)
markup_assistant.row(button8)


count_matches = {'england' : 38, 'germany' : 34, 'italy' : 38, 'spain' : 38, 'france' : 38, 'USA' : 34, 'arabia' : 34}