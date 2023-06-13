# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или 
# фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
# и удаления данных.

import random
import os

def CreatePhoneBook():
    file_path = 'phone_book.txt'
    with open(file_path, 'a', encoding='utf-8') as phone_book:
        word = 'да'
        while word == 'да':
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            patronymic = input('Введите отчество: ')
            phone_number = str(random.randint(1000001, 9999999))
    
            phone_book.write(last_name.encode('utf-8').decode('utf-8') + '\n')
            phone_book.write(first_name.encode('utf-8').decode('utf-8') + '\n')
            phone_book.write(patronymic.encode('utf-8').decode('utf-8') + '\n')
            phone_book.write(phone_number + '\n')

            word = input('Хотите продолжить ввод данных? ')
        print('Данные добавлены в phone_book.txt')



def ReadPhoneBook():
    file_path = 'phone_book.txt'
    with open(file_path, 'r', encoding='utf-8') as phone_book:
        last_name = phone_book.readline()
        while last_name != '':
            last_name = last_name.rstrip('\n')
            first_name = (phone_book.readline()).rstrip('\n')
            patronymic = (phone_book.readline()).rstrip('\n')
            phone_number = (phone_book.readline()).rstrip('\n')
            print('Фамилия:', last_name)
            print('Имя:', first_name)
            print('Отчество:', patronymic)
            print('Номер телефона:', phone_number)
            print()
            last_name = phone_book.readline()
        
def RecordSearch():
    found = False
    search = input('Введите искомую Фамилию: ')
    print()
    file_path = 'phone_book.txt'
    with open(file_path, 'r', encoding='utf-8') as phone_book:
        last_name = phone_book.readline()
        while last_name != '':
            last_name = last_name.rstrip('\n')
            first_name = (phone_book.readline()).rstrip('\n')
            patronymic = (phone_book.readline()).rstrip('\n')
            phone_number = (phone_book.readline()).rstrip('\n')
            if last_name == search:
                print('Фамилия:', last_name)
                print('Имя:', first_name)
                print('Отчество:', patronymic)
                print('Номер телефона:', phone_number)
                print()
                found = True
            last_name = phone_book.readline()
        if not found:
            print('искомая Фамилия в файле не найдена')

def RecordChange():
    found = False
    search = input('Введите искомую Фамилию: ')
    new_phone_number = str(random.randint(1000001, 9999999))
    print()
    phone_book = open('phone_book.txt', 'r', encoding='utf-8')
    phone_book_temp = open('phone_book_temp.txt', 'w', encoding='utf-8')
    last_name = phone_book.readline()
    while last_name != '':
        last_name = last_name.rstrip('\n')
        first_name = (phone_book.readline()).rstrip('\n')
        patronymic = (phone_book.readline()).rstrip('\n')
        phone_number = (phone_book.readline()).rstrip('\n')
             
        if last_name == search:
            phone_book_temp.write(last_name + '\n')
            phone_book_temp.write(first_name + '\n')
            phone_book_temp.write(patronymic + '\n')
            phone_book_temp.write(new_phone_number + '\n')

            found = True

        else:
            phone_book_temp.write(last_name + '\n')
            phone_book_temp.write(first_name + '\n')
            phone_book_temp.write(patronymic + '\n')
            phone_book_temp.write(phone_number + '\n')

        last_name = phone_book.readline()
    phone_book.close()
    phone_book_temp.close()

    os.remove('phone_book.txt')
    os.rename('phone_book_temp.txt', 'phone_book.txt')
            
    if found:
            print('Файл обновлён')
    else:
            print('эта Фамилия в файле не найдена')



def RecordDelete():
    found = False
    search = input('Какую Фамилию желаете удалить?: ')

    phone_book = open('phone_book.txt', 'r', encoding='utf-8')
    phone_book_temp = open('phone_book_temp.txt', 'w', encoding='utf-8')
    last_name = phone_book.readline()
    while last_name != '':
        last_name = last_name.rstrip('\n')
        first_name = (phone_book.readline()).rstrip('\n')
        patronymic = (phone_book.readline()).rstrip('\n')
        phone_number = (phone_book.readline()).rstrip('\n')
             
        if last_name != search:
            phone_book_temp.write(last_name + '\n')
            phone_book_temp.write(first_name + '\n')
            phone_book_temp.write(patronymic + '\n')
            phone_book_temp.write(phone_number + '\n')

            found = True
        last_name = phone_book.readline()

    phone_book.close()
    phone_book_temp.close()

    os.remove('phone_book.txt')
    os.rename('phone_book_temp.txt', 'phone_book.txt')
            
    if found:
        print('Файл обновлён')


            
a = int(input('1 - ввод данных, 2 - вывод данных, 3 - поиск данных, 4 - изменение данных, 5 - удаление данных \n'))
if a == 1:
    CreatePhoneBook()
elif a == 2:
    ReadPhoneBook()
elif a == 3:
    RecordSearch()
elif a == 4:
    RecordChange()
elif a == 5:
    RecordDelete()

