# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random
N = int(input("Введите кол-во элементов в списке N = "))
list = []
for i in range(N):
    i = random.randint(1, 5)
    list.append(i)
print(list)

X = int(input("Введите число X = "))
count = 0
for n in list:
    if n == X:
        count = count + 1
print(f"Число {X} встречается в списке {count} раз(а)")



