# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).

import random

def DefineIndex(list, min, max):
      for i in range(N):
        if (list[i] >= min) and (list[i] <= max):
          print(i, end = ' ')

list = []
N = 10
for k in range(N):
  list.append(random.randint(1, 20))
print(list)

min = int(input('Минимум диапазона: '))
max = int(input('Максимум диапазона: '))

DefineIndex(list, min, max)


        

