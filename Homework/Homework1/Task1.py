#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
def list_create(N):
    list = []
    for i in range(0,N):
        list.append((-3)**i)
    return(list)

print(list_create(5))