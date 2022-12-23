# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 

import random

n = int(input())

array_n = [random.randint(1, n) for i in  range(n)]

print (array_n)

result = 0

for i in range(1, n, 2):
    
    result += array_n[i]

print( result)