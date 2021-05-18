import types

import telebot
bot = telebot.TeleBot('1803169743:AAEeazoOd8OraGEWNCLKQWgEH8Xv0iQKuCw')


# приветственное письмо
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('1⃣ Начать 1⃣  ')
    bot.send_message(message.from_user.id, 'Добрый день! Я - IngoBot и я помогу Вам в любом вопросе!', reply_markup=user_markup)


# вкладка быстрого доступа
@bot.message_handler(commands=['text'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Купить страховой полис", switch_inline_query="Telegram")
    keyboard.add(switch_button)
    bot.send_message(message.chat.id, "Пожалйста, выберите тематику обращения", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
print(123)
