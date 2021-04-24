import telebot
bot = telebot.TeleBot('1803169743:AAEeazoOd8OraGEWNCLKQWgEH8Xv0iQKuCw')


# приветственное письмо
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Добрый день, {message.from_user.first_name}! Я - IngoBot и я помогу Вам в любом вопросе!')


# вкладка быстрого доступа
@bot.message_handler(commands=['text'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Купить страховой полис", switch_inline_query="Telegram")
    keyboard.add(switch_button)
    bot.send_message(message.chat.id, "Пожалйста, выберите тематику обращения", reply_markup=keyboard)
