# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке.

def RhythmDefinition(str):
    str = str.lower()
    list_1 = str.split()
    list_2 = []
    for phrase in list_1:
        count = 0
        for i in range(len(phrase)):
            if phrase[i] in 'ауоыэяюёие':
                count = count + 1
        list_2.append(count)
    set_1 = set(list_2)
    if len(set_1) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


                       
        
        
    
RhythmDefinition('пАра-ра-рам рам-пам-папам па-ра-па-па до-Рэ-ми-ФА')