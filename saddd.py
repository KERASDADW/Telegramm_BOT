import telebot
from telebot import types

token = '5266573315:AAECK4dHbC7p5ALi7gDcCHRv0_MFr4g8zNs' #bot token from @botFather

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
 keyboard = types.ReplyKeyboardMarkup()
 keyboard.row("/start", "/help", "/test", "/Youtube")
 # RUN
 bot.send_message(message.chat.id, 'Привет давно не виделись', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
 bot.send_message(message.chat.id, "Здравствуйте, пока я могу \n/start - начать общение\n/help - команды, которые я могу выполнить\n/test - средняя оценка которая была в школе \n/Youtube - ссылка на видеохостинг")

@bot.message_handler(commands=['test'])
def start_message(message):
 markup = telebot.types.InlineKeyboardMarkup()
 markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
 markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
 markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
 bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)

@bot.message_handler(commands=['Youtube'])
def start_message(message):
 bot.send_message(message.chat.id, 'https://www.youtube.com/')

@bot.message_handler(content_types=['text'])
def answer(message):
 if message.text.lower() == "привет":
  bot.send_message(message.chat.id, 'Ну здравствуй')
 if message.text == "чего делаешь ?":
  bot.send_message(message.from_user.id, "с тобой разговариваю")
 if message.text == 'как дела ?':
  bot.send_message(message.chat.id, 'Нормально Нормально')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '3':
        answer = 'Вы троечник!'
    elif call.data == '4':
        answer = 'Вы хорошист!'
    elif call.data == '5':
        answer = 'Вы отличник!'

    bot.send_message(call.message.chat.id, answer)
bot.polling(none_stop = True)