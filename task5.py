# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int (input())

def positive(n):
    positive_array = [1,1]
    for i in range (n-2):
        positive_array.append(positive_array[-2]+positive_array[-1])
    return positive_array

def negative(n):
    negative_array = [0,1]
    for i in range (n-1):
        negative_array.append(negative_array[-2]-negative_array[-1])
    return negative_array[::-1] # перевернули массив


print(negative(n)+positive(n))