import telebot
import telebot.types

bot = telebot.TeleBot('1803169743:AAEeazoOd8OraGEWNCLKQWgEH8Xv0iQKuCw')

# словарь ответов на вопросы
ingo_qa = {'Чем отличается электронный полис от бумажного?': 'Только удобством покупки и получения. Электронный полис нельзя потерять. Вы можете в любой момент его распечатать. Электронный полис является полноценным документом.',
           'Нужно ли получать печатную версию электронного полиса?': 'Нет, электронный полис имеет такую же силу, как традиционный полис, приобретенный в офисе. Полис придет на e-mail, который Вы укажете при оформлении. Вы можете просто распечатать полис на обычном принтере, что бы он был у Вас под рукой или воспользоваться личным кабинетом, в котором всегда можно получить доступ к электронной версии полиса',
           'Как оплатить полис?': 'Для оплаты полиса Вам необходимо рассчитать стоимость с помощью калькулятора по выбранному продукту, для оформления - заполнить анкету, нажать кнопку «Оплатить» для оплаты банковской картой или «Оплатить другим способом» для оплаты электронными деньгами, через терминалы оплаты, салоны связи или интернет банкинг. Вы будете перенаправлены на защищенную страницу платежной системы для оплаты, где Вам необходимо будет ввести данные Вашей карты или выбрать другой способ оплаты.',
           'Какие полисы я могу купить на сайте?': 'С полным списком продуктов, доступных для покупки онлайн, можно ознакомиться в нашем интернет-магазине.',
           'Как обеспечивается сохранность персональных данных?': 'Все введенные персональные данные клиентов хранятся на нашем защищенном сервере, доступ к данным имеют только специалисты нашей компании.',
           'Как я могу удостовериться в подлинности электронного полиса?': 'Высланный Вам страховой полис подписан СПАО «Ингосстрах» с использованием квалифицированной электронной цифровой подписи, удостоверяющей подлинность этого документа по алгоритму ГОСТ Р 34.10-2001.',
           'Что делать, если полис был оплачен, но не пришел на указанный при оформлении e-mail?': 'В случае если оплаченный полис не пришел на указанный Вами e-mail, необходимо проверить папку «спам» или «нежелательная почта», также необходимо проверить спам-фильтр Вашего почтового сервера и списание денежных средств в Вашем банке. Если письмо с полисом не обнаружено в папках с нежелательной почтой (спамом), и при этом деньги со счета были списаны, необходимо связаться с нами по телефону 8 (495) 956-55-55 или оставить заявку на звонок и мы сами свяжемся с Вами для повторной отправки полиса.',
           'Какие полисы можно продлить онлайн?': 'Продлить в режиме онлайн на сайте возможно полисы КАСКО и страхования квартир. Продление возможно на условиях предыдущего договора. Если требуется внести изменения в условия, обратитесь к представителю компании или воспользуйтесь разделом «Продление» в личнном кабинете (только по договорам ИФЛ (квартиры и ответственность) и КАСКО).',
           'Как продлить полис через сайт?': 'Продлить полис КАСКО или ИФЛ можно на соответствующей странице сайта. Вам потребуется номер страхового полиса и фамилия того, кто заключал договор (страхователя).'}
# словарь для прощания
buy_qa = {'Спасибо. Всего доброго!': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'Всего доброго': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'Всего доброго!': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'До свиданья': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'Спасибо': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'cпасибо': 'Рад был Вам помочь! Всего доброго и хорошего дня!',
          'всего доброго': 'Рад был Вам помочь! Всего доброго и хорошего дня!'
          'до свиданья': 'Рад был Вам помочь! Всего доброго и хорошего дня!'}

# приветственное письмо
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/Начать')
    bot.send_message(message.from_user.id, 'Добрый день, '+ message.from_user.first_name +'! Я - IngoBot и я помогу Вам в любом вопросе!', reply_markup=user_markup)

# Ответ на вопросы (1 вариант из словаря/ 2 вариант - ошибка)
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print(message.from_user.first_name)
    bot.send_chat_action(message.from_user.id, 'typing')
    print(message.text)
    if message.text in ingo_qa.keys():
        bot.reply_to(message, ingo_qa.get(message.text))
    elif message.text in buy_qa.keys():
        bot.reply_to(message, buy_qa.get(message.text))
    else:
        bot.reply_to(message, "Я не понимаю, что такое {!s}! Перефразируйте!".format(message.text))


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



# постоянная обработка информации
bot.polling(none_stop=True, interval=0)
print(123)