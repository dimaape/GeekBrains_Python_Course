# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


digit = int(input("Введите число:\n--> "))

last = digit % 10
while digit > 0:
    val = digit % 10
    if val > last:
        last = val
    digit = digit // 10
print(last)
