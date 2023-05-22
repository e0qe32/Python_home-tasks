# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число: "))
degree = 1
for i in range (1, N):
    degree = degree * 2
    if degree < N:
        print(degree)
    else:
        break
    