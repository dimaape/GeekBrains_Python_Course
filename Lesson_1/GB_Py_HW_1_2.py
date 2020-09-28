# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


user_input_seconds = int(input("Please provide seconds:\n--> "))
hours = user_input_seconds // 3600
minutes = (user_input_seconds - (hours * 3600)) // 60
seconds = user_input_seconds % 60

print(f'{hours:02d}' + ":" + f'{minutes:02d}' + ":" + f'{seconds:02d}')

