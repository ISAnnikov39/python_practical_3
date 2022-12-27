# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int (input())


def binary (n, resulte = ""):
    if n == 0:
        return resulte
    else:
        resulte = resulte + str(n%2)
        return binary(n//2, resulte)
    
print (binary(n))