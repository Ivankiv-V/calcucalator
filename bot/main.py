import telebot.types

import telebot
bot = telebot.TeleBot('1803169743:AAEeazoOd8OraGEWNCLKQWgEH8Xv0iQKuCw')


# приветственное письмо
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/Начать')
    bot.send_message(message.from_user.id, 'Добрый день, '+ message.from_user.first_name +'! Я - IngoBot и я помогу Вам в любом вопросе!', reply_markup=user_markup)


# вкладка быстрого доступа
@bot.message_handler(commands=['Начать'])
def any_msg(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    switch_button1 = telebot.types.InlineKeyboardButton(text="Купить страховой полис", switch_inline_query="Telegram")
    keyboard.add(switch_button1)
    switch_button2 = telebot.types.InlineKeyboardButton(text="Вопросы по страховому полису", switch_inline_query="Telegram")
    keyboard.add(switch_button2)
    switch_button3 = telebot.types.InlineKeyboardButton(text="Страховой случай", switch_inline_query="Telegram")
    keyboard.add(switch_button3)
    switch_button4 = telebot.types.InlineKeyboardButton(text="Жалобы и предложения", switch_inline_query="Telegram")
    keyboard.add(switch_button4)
    switch_button5 = telebot.types.InlineKeyboardButton(text="Другое", switch_inline_query="Telegram")
    keyboard.add(switch_button5)
    bot.send_message(message.chat.id, "Пожалйста, выберите тематику обращения", reply_markup=keyboard)

# Для ответа на непонятное обращение
@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, "Я не понимаю, что такое {!s}! Перефразируй!".format(message.text))

@bot.edited_message_handler(func=lambda message: True)
def edit_message(message):
    bot.edit_message_text(chat_id=message.chat.id,
                            text="Я не понимаю, что такое {!s}! Перефразируй!".format(message.text),
                            message_id=message.message_id + 1)


bot.polling(none_stop=True, interval=0)
print(123)