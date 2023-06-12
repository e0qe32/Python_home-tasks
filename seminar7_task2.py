# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая 
# принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы 
# num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной 
# операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def PrintOperationTable(operation, numRows=6, numColumns=6):
    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            if operation(1,1)==2:
                column=column-1
            print(operation(row,column), end='\t')
        print()

print(PrintOperationTable(lambda x,y: x * y))
    