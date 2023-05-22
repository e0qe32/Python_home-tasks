#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
#вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

# 1 - решка
# 0 - герб

n = int(input("На столе лежат монеты в количестве: "))
count = 0 #число монет, которое нужно перевернуть
for i in range(1, n+1):
    side = int(input(f"Какой стороной обращена {i}-я монета 1-решка, 0-герб: "))
    if side == 0:
        count = count + 1
print(f"Кол-во монет, которые нужно перевернуть равно {count}")
