# Задание 1.1

# Поработайте с переменными, создайте несколько, выведите на экран
print("Поработайте с переменными, создайте несколько, выведите на экран.\n")
var_a = 0
var_b = "some text"
var_c = 10
var_d = "some text again"

print(var_a, var_b, var_c, var_d, sep='\n')

# Запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print("\nЗапросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.\n" +
      "Нет обработчика ошибок. Но это и не в данном уроке.\n")

user_input_int_a = int(input("Please provide any integer:\n--> "))
user_input_float_a = float(input("Please provide any float number:\n--> "))
user_input_str_a = str(input("Please provide any string:\n--> "))
user_input_str_b = str(input("Please provide another string:\n--> "))

print(user_input_int_a, user_input_float_a, user_input_str_a, user_input_str_b, sep='\n')




