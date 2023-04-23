# print('hello')
# name = "Ivan"
# age = 23
# print(4 % 3)
# print(8 // 3)
# name = input("Введите ваше имя")
# a = "1234"
# b = int(a)
# print(type(b))
# num = int(input("введите целое число"))
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input("введите целое число"))
# data.sort()
# print(data)
# string = "Hello"
# res = string.upper()
# print(res)
# name = "Ivan"
# for i in name:
#     print(i)
# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")
# print("Привет", first_name, last_name, "?")

# a = 3.14
# b = '3.14'
# print(type(a))
# # <class 'float'>
# print(type(b))
# print(0.1+0.1*5-0.3*4)
# print ((3.14+0.3)/2+0.15)
# t = (0,1,2)
# t[1] += 1
# a = 5//2
# print(a)
# print (31 % 2 + 31 % 2)
# print (13 % 3 * 3 - 3**2)
# pi = 3.14*2
# print(round(pi))
#
# #numbers_split = numbers.split()
# numbers_joined = '\n' .join(numbers_split)
# print(numbers_joined)
# age = 5.1234
# try_age = "I'm %f years old" % (age)
# print(try_age)
# pi = 31.4159265
# print ("%.4e" % (pi))
# print("d%/d%/d%"% (hours, minutes, second))
# string = input("Введите числа через пробел:")
# list_of_strings = string.split()
# list_of_numbers = list(map(int, list_of_strings))
# print(sum(list_of_numbers[::3]))
# L = list(map(float, input().split()))
# L[0], L[-1] = L[-1], L[0]
# print(L)
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))
# L = ['a', 'b', 'c']
# print(id(L))
# L.append('d')
# print(id(L))
# a = 5
# b = 3 + 2
# print(id(a) - id(b))
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b)
# a_and_b =a_set.union(b_set)
# print(a_and_b)
money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(int(per_cent[key] * money / 100))
max_deposit = int(max(deposit))
print(deposit)
print("Максимальная сумма, которую вы можете заработать - " + str(max_deposit))