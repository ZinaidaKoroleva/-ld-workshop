# Реализуйте алгоритм перемешивания списка.
# import random
# list = [1,2,3,4]
# random.shuffle(list)
# print(list)

# Реализовать алгоритм задания случайного числа без генератора случайных чисел.
# import time
# seconds = int(time.time_ns()*1000.0)
# print(int(seconds)%100)

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

# def num(a):
#     sum = 0
#     for i in range (1,a+1):
#         n = (1+ 1/i)**i
#         sum += n
#     print(round(sum,3))
# num(5)

# Задайте список. Напишите программу, котоая определит, присутствует ли в заданном списке строк некое число
# ['geek', 'brains4', '5five', '3 friends']

def find(originalList,number):
    #print([int(number) for number in originalList if number.isdigit()])
    for i in originalList:
        if i.find(str(number)) >= 0:
            return print(f"Число {number} есть в списке")
    return print(f"Числа {number} нет в списке")
list = 'geek', 'brains4', '5five', '3 friends'
find(list, 3)