# 1.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
# import random

# list_random = []

# length_list = random.randint(5,20)
# for i in range(length_list):
#     list_random.append(random.randint(1,101))
# # list.sort()
# print(list_random)

# list_str = "\n".join(map(str,list_random))

# with open('random_values.txt', 'w') as fp:
#     fp.write(list_str)

# new_list = []
# with open('random_values.txt', 'r') as fp:
#     new_list = fp.readlines()
#     new_list = list(map(int,new_list))
#     new_list.sort()

# print(new_list)

# sorted_string = "\n".join(map(str,new_list))
# with open('random_values.txt', 'w') as fp:
#     fp.write(sorted_string)

# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

list_of_numbers = [5, 2, 3, 4, 6, 1, 7]
sorted_list = []

if list_of_numbers[0] < list_of_numbers[1]:
    sorted_list.append(list_of_numbers[0])
else:  sorted_list.append(list_of_numbers[1])

for i in range(2,len(list_of_numbers)):
    if list_of_numbers[i]> list_of_numbers[i-1]:
        sorted_list.append(list_of_numbers[i])

    if list_of_numbers[i] < list_of_numbers[i-1] and list_of_numbers[i] > list_of_numbers[i-2]:
            # sorted_list.pop([])
            sorted_list.append(list_of_numbers[i])

print(sorted_list)

# list_of_numbers = [1, 5, 2, 3, 4, 6, 1, 7]

# if list_of_numbers[0] > list_of_numbers[1]:
#     list_of_numbers.pop(list_of_numbers[0])

# for i in range(2,len(list_of_numbers)):
    
#     if (list_of_numbers[i] < list_of_numbers[i-1]) and (list_of_numbers[i] > list_of_numbers[i-2]):
#         list_of_numbers.pop([i-1])
#         i = i-1
            

# print(list_of_numbers)