# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_input_digit = int(input("Please provide any int digit:\n--> "))
result = user_input_digit + int(str(user_input_digit) + str(user_input_digit))\
         + int(str(user_input_digit) + str(user_input_digit) + str(user_input_digit))
print(result)
