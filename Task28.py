# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('А - Введите число: '))
b = int(input('В - Введите второе число: '))

def count_sum(a, b):
    res = 0
    for i in range(a):
        if i < a:
            res += 1
    for i in range(b):
        if i < b:
            res += 1
    return res
res = count_sum(a, b)
print(res)