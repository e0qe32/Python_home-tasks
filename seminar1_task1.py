# Задача 2: Найдите сумму цифр трехзначного числа.

string = input("Введите трехзначное число: ")
if len(string) == 3:
  summa = int(string[0]) + int(string[1]) + int(string[2])
  print(f"Сумма цифр числа {string} равна {summa}")
else:
  print("Число не трехзначное")
  
