#библиотека телеграм
import telebot 

#токен зарегистрированного у @BotFather нового бота
token = '5640805430:AAHAJNMMhSpBgyW4eyLkpOAZFoZFTwKp_ds' #убрал в этом файле, в продакшене ставил свой.

#создаем бота
bot = telebot.TeleBot(token)

#переменные
HELP = """
/help - список команд бота.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи."""

tasks = {}

#функция добавления задачи
def add_todo(date, task):
	if date in tasks:
		tasks[date].append(task)
	else:
		tasks[date] = []
		tasks[date].append(task)
	print("Задача ", task, " добавлена на ", date)

#функции бота
#обработчик значения сообщения, в данном случае команды /help или /start
@bot.message_handler(commands=['help', 'start']) 
def help(message):
	bot.send_message(message.chat.id, HELP)

#обработка команды /add
@bot.message_handler(commands=['add'])
def add(message):
	#команда разделяет строки по пробелам и добавляет в список
	command = message.text.split(maxsplit=2) #maxsplit делит строку на 2 части.
	date = command[1].lower() #чтобы дата была всегда в нижнем регистре
	task = command[2]
	if len(task) < 3:
		text = 'Слишком короткое название задачи'
	else:
		add_todo(date, task)
		text = 'Задача ' + task + ' добавлена на дату ' + date
	bot.send_message(message.chat.id, text)

#обработка команды /show
@bot.message_handler(commands=['show'])
def show(message): #message.text = /show <date>
	command = message.text.split(maxsplit=1)
	date = command[1].lower()
	text = ''
	if date in tasks:
		text = date.upper() + '\n'
		for task in tasks[date]:
			text = text + '[] ' + task + '\n'
	else:
		text = 'Задач на эту дату нет.'
	bot.send_message(message.chat.id, text)


#цикл запросов на сервер телеграм, чтобы бот проверял отправили ли ему сообщение
bot.polling(none_stop = True) 
