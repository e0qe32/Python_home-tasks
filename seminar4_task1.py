# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами элементы множеств.

import random

N = int(input("Введите кол-во элементов в списке N = "))
list_N = []
for i in range(N):
    i = random.randint(1, 20)
    list_N.append(i)
print(list_N)
Set_N = set(list_N)
print()


M = int(input("Введите кол-во элементов в списке M = "))
list_M = []
for j in range(M):
    j = random.randint(1, 20)
    list_M.append(j)
print(list_M)
print()

List_U = list(Set_N.union(set(list_M)))
List_U.sort()

print(List_U)


