HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(today)
    print(tomorrow)
    print(other)
  elif command == "add":
    task = input("Введите название задачи: ")
    date = input("cегодня? завтра? бессрочно?")
    print(date)
    if date == "сегодня":
      today.append(task)
    elif date == "завтра":
      tomorrow.append(task)
    else:
      other.append(task)
    print("Задача добавлена")
  elif command == 'exit':
    print('Спасибо за использование! До свидания!')
    break
  else: 
    print("Неизвестная команда")
    break

print("До свидания!")