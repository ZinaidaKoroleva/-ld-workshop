# 1.	Найти НОК двух чисел
def aliquot(a,b):
    if a > b:
        max = a
    else:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            aliquot = max
            break
        max += 1
    return aliquot

number_one = 12
number_two = 13

print("Наименьшее общее кратное: " , aliquot(number_one,number_two))

# 2.	Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# import math

# def pi(d):
#     k = 1
#     x = 0
#     while abs(math.pi - x) > d:
#         x = x +4 * ((-1)**(k+1))/(2*k - 1)
#         k += 1
#     return x

# d = 0.001
# print(pi(d))

# 3.	Составить список простых множителей натурального числа N
# def multipliers(n):
#     multipliers_list = [1]
#     m = 2
#     while (n > 1):
#         while (n % m == 0):  
#             multipliers_list.append(m)
#             n = n // m
#         m += 1    
#     return multipliers_list
# N = 144
# print(f'Простые множители числа {N} : {multipliers(N)}')

# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# def delete_repeat(elements):
#     return set(elements)

# list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(delete_repeat(list))

# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# def delete_even_numbers():
#     with open(r'C:\Users\shymk\OneDrive\Рабочий стол\python\Homework\Homework3\file.txt', 'r') as fp:
#         list = fp.readlines()
#         for i in range(len(list)):
#              list[i] = int(list[i])
#         print(list)

# # Выясняем длину нового списка
#         count = 0
#         for i in range(len(list)):
#             if list[i] % 2 == 0:
#                 count += 1 

#         length = len(list) - count
#         for i in range(length):
#             if list[i] % 2 == 0:
#                 del list[i]
#         print(list)
#     list_write = " ".join(map(str,list))
#     with open(r'C:\Users\shymk\OneDrive\Рабочий стол\python\Homework\Homework3\file.txt', 'w') as fp:
#         fp.write(list_write)

# delete_even_numbers()


    