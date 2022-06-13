# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# arithmetic_example = '(1+2)*3'

# def delete_space(input_string):
#     input_string = input_string.replace(' ', '')  # убираем пробелы

# def find_braces(string):      # метод,находящий скобки.операции в скобках будут приоритетны
#     for i in range(0,len(string)):
#         if string[i] == '(':
#             opens_brace = string[i]
#         if string[i] == ')':
#             closes_brace = string[i]
#     return opens_brace,closes_brace


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.

# Не использовать функцию encode.

def code(input_string):
    code_string = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for symb in input_string:
        ind = alphabet.find(symb.lower())
        if ind != -1:
            letter = alphabet[(ind + 13)%len(alphabet)]
        else:
            letter = symb
        code_string += letter
    return code_string

def decode(input_string):
    code_string = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for symb in input_string:
        ind = alphabet.find(symb.lower())
        if ind != -1:
            letter = alphabet[(ind - 13)%len(alphabet)]
        else:
            letter = symb
        code_string += letter
    return code_string

code_text = 'Карл у клары украл кораллы'
decipher_text = 'чмэш а чшмэз ачэмш чыэмшшз'

print(code(code_text))               
print(decode(decipher_text))