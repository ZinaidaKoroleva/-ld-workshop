# 1.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
import random

list_random = []

length_list = random.randint(5,20)
for i in range(length_list):
    list_random.append(random.randint(1,101))
# list.sort()
print(list_random)

list_str = "\n".join(map(str,list_random))

with open('random_values.txt', 'w') as fp:
    fp.write(list_str)

new_list = []
with open('random_values.txt', 'r') as fp:
    new_list = fp.readlines()
    new_list = list(map(int,new_list))
    new_list.sort()

print(new_list)

sorted_string = "\n".join(map(str,new_list))
with open('random_values.txt', 'w') as fp:
    fp.write(sorted_string)

# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

# previous_number = list[0]
# if list[i]> previous_number:
