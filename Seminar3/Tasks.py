## 1. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
## Позиции хранятся в файле file.txt в одной строке одно число
# from array import array
# from operator import mul
# from functools import reduce
# from random import randint 

# def count_prod():
#     with open(r'C:\Users\shymk\OneDrive\Рабочий стол\python\Seminar3\file.txt', 'r') as position:
#         pos = position.readlines()

#         for i in range(len(pos)):
#             pos[i] = int(pos[i])

#     N = max(pos) + 2

#     with open(r'C:\Users\shymk\OneDrive\Рабочий стол\python\Seminar3\file.txt', 'a') as position:
#         position.write(str(N) + '\n')
#     array = [randint(-N,N) for i in range(N)]
#     # prod = 1
#     # for val in pos:
#     #     prod *= array[val]
#     prod = reduce(mul,[array[val] for val in pos])
#     print(array)
#     print(prod)
#     print(pos)


# count_prod()

## 2. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
## Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fib(n):
#     if n in (0,1):
#         return n
#     length = n + 1
#     fibs_pos = [0]*length
#     fibs_pos[1] = 1
#     for i in range (2, length):
#         fibs_pos[i] = (fibs_pos[i-1]+ fibs_pos[i-2])

#     fibs_neg = [0]*length
#     fibs_neg[1] = 1
#     for i in range(2, length):
#         fibs_neg[i] = fibs_neg[i-2] - fibs_neg[i-1]
#     fibs_neg.reverse()

#     return fibs_neg + fibs_pos[1:]

# f_n = 8
# print(f"Fib: {fib(f_n)}")
## 3. Строка содержит набор чисел. Показать большее и меньшее число
## Символ-разделитель - пробел
# from cmath import sqrt

# string = "1 3 5 98 -876 9"
# numb = string.split(' ')
# for i in range(len(numb)):
#     numb[i] = int(numb[i])
# print(numb)
# print(max(numb))
# print(min(numb))
## 4. Найти корни квадратного уравнения Ax² + Bx + C = 0

# D = B^2 - 4 ac
# (-B + sqrt(D))/2*A

import math


def quar(a,b,c):
    desc = b**2 - 4*a*c
    x1 = (-b + math.sqrt(desc))/(2*a)
    x2 = (-b - math.sqrt(desc))/(2*a)
    return (x1, x2)

print(quar(1,-4,1))