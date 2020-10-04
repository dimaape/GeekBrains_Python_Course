# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# На списке
seasons = ["Зима", "Весна", "Лето", "Осень"]
months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
user_input = int(input("Введите целое число: "))

for i in zip(seasons, months):
    if user_input in i[1]:
        print(i[0])

# На словаре
seasons_dict = dict(zip(seasons, months))

for i in seasons_dict:
    if user_input in seasons_dict.get(i):
        print(i)


