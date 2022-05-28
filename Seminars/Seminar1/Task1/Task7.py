# Проверить истинность утверждения -(X v Y v Z)= -X ^ -Y ^ -Z для всех значений предикат


for x in range(0,2):
    for y in range (0,2):
        for z in range (0,2):
            left = not(x or y or z)
            right = not x and not y and not z
            statement = left == right
            print (statement)