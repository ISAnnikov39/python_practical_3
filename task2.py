# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


n = int(input())

array_n = [random.randint(0, 10) for i in range(n)]

print (array_n)

pow_list = []

for i in range(len(array_n)//2 + len(array_n)%2):

    pow_list.append(array_n[i]*array_n[-i-1])
    
print (pow_list)