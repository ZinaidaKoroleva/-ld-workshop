# 2. Напишите программу, котррая на вход принимает 5 чисел и находит максимальное из них.
def number(a,b,c,d,f):
    max = 0
    if (a>b) and (a>c) and (a>d) and (a>f):
        max = a
    elif (b>c) and (b>d) and (b>f):
        max = b
    elif (c>d) and (c>f):
        max = c
    elif (d>f):
        max = d
    else: 
        max = f

    print(f"max = {max}")

number(11,23,3,48,51)

