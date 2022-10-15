#библиотека телеграм
import telebot

#токен зарегистрированного у @BotFather нового бота
token = 'ваш токен' #убрал в этом файле, в продакшене ставил свой.

#создаем бота
bot = telebot.TeleBot(token)

#любое текстовое сообщение функции echo будет обрабатываться
@bot.message_handler(content_types=['text']) 

#функция бота
def echo(message):
	myName = 'Alex'
	if myName in message.text == 'Alex':
		bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
	else:
		bot.send_message(message.chat.id, message.text)

#цикл запросов на сервер телеграм, чтобы бот проверял отправили ли ему сообщение
bot.polling(none_stop = True) 
