# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.

a = int(input('А - Введите число: '))
b = int(input('В - Введите в какую степень возвести число: '))

res = 1
for i in range(b):
    if i < b:
        res *= a
print(res)
