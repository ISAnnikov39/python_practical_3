# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

arr = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(len(arr)):
     
     arr[i] = round(arr[i]- int(arr[i]), 2)

print(arr)

min_arr = arr[1]

max_arr = arr[0]

for i in range (1,len(arr)):

    if (arr[i] > arr[i-1]):

        temprorary = arr[i-1]

        arr [i-1] = arr[i]

        min_arr = arr [i-1]

        arr[i-1] = temprorary

print(min_arr)

for i in range (1,len(arr)):

    if (arr[i-1] > arr[i]):

        temprorary = arr[i]

        arr [i] = arr[i-1]

        max_arr = arr [i]

        arr[i-1] = temprorary

print (max_arr)

print(max_arr-min_arr)