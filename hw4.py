# задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# - 
n = int(input('Введите число: '))
i = 0
f=1
f_1=f_2=0
fibo=list()
fibo.append(0)
fibo.append(1)
fibo.insert(0,1)
while i<n-1:
    f_1=f_2
    f_2=f
    f=f_1+f_2
    fibo.append(f)
    i+=1
j=0
fm=1
f_1=f_2=0
while j<n-1:
    f_1=f_2
    f_2=fm
    fm=(f_1-f_2)
    fibo.insert(0,fm)
    j+=1
print(fibo)
