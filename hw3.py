# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . Но теперь количество предикатов 
# не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, проверяем 
# это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа. 
# В конце вывести результат проверки истинности этого утверждения.

import time
time1= time.time()
i=0
while i<100:
    for x1 in [True,False]:
        for x2 in [True,False]:
            for x3 in [True,False]:
                for x4 in [True,False]:
                    for x5 in [True,False]:
                        for x6 in [True,False]:
                            for x7 in [True,False]:
                                for x8 in [True,False]:
                                    for x9 in [True,False]:
                                        for x10 in [True,False]:
                                            if not (x1 or x2 or x3 or x4 or x5 or x6 or x7 or x8 or x9 or 
                                                    x10) == (not x1 and not x2 and not x3 and not x4 and 
                                                            not x5 and not x6 and not x7 and not x8 and not x9 and not x10):
                                                print('OK')
                                            else:
                                                print('Утверждение неверно')
                                                break 
                                                
    i+=1                                         

time2= time.time()
print(time2-time1)
