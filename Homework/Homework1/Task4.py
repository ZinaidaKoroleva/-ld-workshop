#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]
def multiplication(N):
    array = [0 for i in range(N)]
    for j in range(0,N):
        if j == 0:
            array[j] = 1
        else:
            array[j] = array[j-1]*(j+1)
    return array

print(multiplication(4))