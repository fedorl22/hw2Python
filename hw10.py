# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random 
n = int(input('Введите количество монеток на столе: '))
money_list =[]
for _ in range(n):
    money_list.append(random.randint(0,1))
print(money_list)
count_orel=0

for money in money_list:
    if money==1:
        count_orel+=1
if count_orel>n-count_orel:
    print('Минимально число =', n-count_orel)
else:
    print('Минимально число =', count_orel)

