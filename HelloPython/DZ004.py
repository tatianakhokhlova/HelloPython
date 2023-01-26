# Создайте список из случайных чисел. 
# Найдите количество различных элементов в нем.

n = [1, 1, 1, 12, -3, -18]
print(len(set(n)))

# 1. Фрукты
#Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

fruits_dict = {}
k = int(input("Введите количество фруктов: "))
for count in range(0, k):
  fruit = input("Введите название фрукта")
  value = input("Введите количество фруктов")
  fruits_dict[fruit] = value
print(fruits_dict)

#2. Старший и младший
#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
#Создайте список friends и добавьте в него N словарей с ключами name и age.
#Найдите самого младшего из друзей и выведите его имя.

n = int(input("Введите количество друзей: "))
friends = []
new_friend = {}
for element in range(0, n):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    new_friend["name"] = name
    new_friend["age"] = age
    friends.append(new_friend)
    new_friend = {}

print("Список Ваших друзей: ", friends)

min_age = friends[0]['age']
for element in friends:
    if element['age'] < min_age:
        min_age = element['age']
for element in friends:
    if element['age'] == min_age:
        print(element['name'])

#3. Еще немного о друзьях
#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
#Создайте список friends и добавьте в него N словарей с ключами name и age.
#Выведите средний возраст всех друзей и самое длинное имя.

n = int(input("Введите количество друзей: "))
friends = []
new_friend = {}
for element in range(0, n):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    new_friend["name"] = name
    new_friend["age"] = age
    friends.append(new_friend)
    new_friend = {}
print("Список Ваших друзей: ", friends)

aver_age = 0
longest_name = friends[0]['name']
for element in friends:
    aver_age = aver_age + element['age']
    if len(element['name']) > len(longest_name):
        longest_name = element['name']
aver_age = aver_age/n
print("Средний возраст Ваших друзей составляет:  ", round(aver_age, 1))
print()
print("Самое длинное имя: ", longest_name)

# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

print('Введите количество слов словаря: ')
print()
n = int(input())
n1 = " слово"
n2 = " слова"
n3 = " слов"
vocabulary = {}
if n >= 0:
    if n == 0:
        print('Введите корректное количество слов')
    elif n%100>=10 and n%100<=20:
        print(f'Введите {n} английских {n3} c переводами: ')
    elif n%10==1:
        print(f'Введите {n} английских {n1} c переводами: ')
    elif n%10>=2 and n%10<=4:
        print(f'Введите {n} английских {n2} c переводами: ')
else:
    print('Введите корректное количество слов')
print()

for i in range(n):
    words = input()
    temp_list = words.split(' - ')
    vocabulary[temp_list[0]] = temp_list[1].split(', ')
print(vocabulary)