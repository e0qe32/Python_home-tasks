# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
import math
import random
N = int(input("Введите кол-во элементов в списке N = "))
list = []
for i in range(N):
    i = random.randint(1, 10)
    list.append(i)
print(list)

X = int(input("Введите число X = "))
for min in range(len(list)):
    for i in range(len(list)):
        diff = math.fabs(X - list[i])
        if diff == min:
            print(list[i])
            

            
        


    
        
    



