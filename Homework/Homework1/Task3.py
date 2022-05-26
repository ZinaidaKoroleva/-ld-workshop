#Подсчитать сумму цифр в вещественном числе.
def summ(N):
    summ = 0
    for i in str(N):
        if i.isdigit():
            summ += int(i)
    return summ

print(f"Сумма цифр в вещественном числе:   {summ(555.55)}")