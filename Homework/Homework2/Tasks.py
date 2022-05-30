# 1.	Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# def sum(list):
#     sum = 0
#     for i in range(0,len(list),2):
#         sum+= list[i]
#     print(f"Сумма чисел списка стоящих на нечетной позиции:   {sum}")

# list_example = [1,2,3,4]
# # Распечатываем исходный список
# for i in range(0,len(list_example)):
#     print(list_example[i])
# sum(list_example)

# 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# def product_of_numbers(list):
#     multiplication_list = []
#     if len(list) % 2 == 0:
#         length = len(list)//2
#     else: 
#         length = len(list)//2 + 1
    
#     for i in range(length):
#          mult=list[i] * list[len(list) - 1 - i]
#          multiplication_list.append(mult)
#     print(multiplication_list)

# list_example = [2, 3, 4, 5, 6]
# list_example2 = [2, 3, 5, 6]
# product_of_numbers(list_example2)

# 3.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def subtraction(list):
    fractional_parts = []
    for i in range(0,len(list)):
        fractional_parts.append(int((list[i]*100)%100))
    max = fractional_parts[0]
    min = fractional_parts[0]
    for i in range(1,len(list)):
        if fractional_parts[i]>max:
            max = fractional_parts[i]
        if  fractional_parts[i] != 0 and fractional_parts[i]<min:
            min = fractional_parts[i]
    subtraction = (max - min)/100
    print(f"Разница между максимальным и минимальным значением дробной части элементов равна {subtraction}")
     
list_example = [1.1, 1.2, 3.1, 5, 10.01]
print(list_example)
subtraction(list_example)
# 4.	Написать программу преобразования десятичного числа в двоичное

# def bin(n):
#     num = ''
#     while n > 0:
#         num = str(n % 2) + num
#         n = n // 2
#     return num

# number = 5

# print(f'Число {number} в двоичной записи = {bin(number)}')