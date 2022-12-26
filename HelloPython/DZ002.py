# Ввести вещественное число и посчитать сумму цифр, 
# из которых оно состоит:

total = input('Введите вещественное число: ')
sum  =  0
for n in total:
    if n.isdigit():
        sum+=int (n)
print(sum)

# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
list = []
f = 1
for i in range(1, n+1):
    f *= i
    list.append(f)
print(list)

# Задайте список из n чисел последовательности
#  (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число: '))
dict = {}
for i in range(1, n+1):
    dict[i] = (1+1/i)**i
print(dict, 'сумма значений равна: ', round(sum(dict.values()), 2))

# Реализуйте алгоритм перемешивания списка
import random
list = [1,2,5,6,7,3,8]
print ('Исходный список: ' + str(list))
for i in range(len(list)-1, 0, -1):
    j=random.randint(0,i+1)
    list[i], list[j] = list[j], list[i]
print('Перемешанный список: ' + str(list))