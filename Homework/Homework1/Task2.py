#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def match(original_text,find_text):

    count = 0
    i = 0
    while i != -1:
        i = original_text.find(find_text,i+1)
        count += 1
    return count

text = input('Исходный текст: ')
symbols = input('Искомая строка: ')
print(match(text,symbols))