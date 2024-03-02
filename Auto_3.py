# my_list = [1,2,3]
# print(my_list)

# sentence = 'What a wonderful life'
# my_list1 = sentence.split(' ')
# print(my_list1)
# my_list2 = list(sentence)
# print(my_list2)

# numbers = [1, 2, 3, 5, 6]
# print(id(numbers))

# for number in numbers:
#     print(number**2)

# print(numbers[0])
# print(numbers[4])
# print(numbers[-1])

# numbers[0] = 10
# print(numbers)
# print(id(numbers))
#numbers2 = [15, 20, 35]
# #append
# numbers.append(numbers2)
# print(numbers)
# print(id(numbers))
#extetd
# numbers.extend(numbers2)
# print(numbers)

# numbers = [1, 2, 3, 5, 6, 4, 10, 9, 10, 10]
# print(id(numbers))
#
# numbers.sort()
# print(numbers)
#
# print(id(sorted(numbers)))
##reverse
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

##get from 1 to 5
# print(numbers[0: 4])
# print(numbers[::-1])

# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

# num2 = []
# for x in numbers:
#     if x%2:
#         num2.append(x*x)
# print(num2)
#
# num3 =[x*x for x in numbers if x%2]
# print(num3)

# print(numbers.count(10))
# print(len(numbers))
#
# l2 = ['a', 2, 2.0, None, 'b']
# print(l2)
# num5 = numbers.copy()
# print(num5)
# print(id(num5))

#TUPLES
# my_tuple = (1, 'apple', None, 2.5)
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple1 = 1,5, 6, 8
# print(my_tuple1)
#
# print(tuple(numbers))

# def func(*args):
#     for item in args:
#         yield item*item
# for i in func(1, 2, 3, 4, 5, 6):
#      print(i)
#
# my_dict = {
#     'first name': 'Alex',
#     'lastname': 'Kim',
#     'age': 30,
#     'department': 'IT'}
#
# print(my_dict)
# print(my_dict['first name'])
#
# my_dict['salary'] = 20000
# print(my_dict)

##SETS

# /HW
#3.1
# my_list = ['a', 'b', [1, 2, 3, 4], 'd']
# print(my_list[2][0])
# print(my_list)

#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0], my_list[2][1], my_list[2][2])

# new_list = my_list[2]
# print(new_list)

# new_list = my_list[2]
# print(*new_list)
#
# new_list = my_list[2]
# print(*new_list, sep='\n')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

#3.2.1
# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# print(list_1[2] + list_1[3] + list_1[5] + list_1[6])
# #3.2.2
# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# strings = []
# digits = []
# for item in list_1:
#     if type(item) == str:
#         strings.append(item)
#     else:
#         digits.append(item)
# print(sum(digits))
#
# for item in strings:
#     if 'a' in item:
#         print(item)
# #3.3   Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# list_b = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list_b))
# # 3.3.1
# list_b = ['cat', 'dog', 'horse', 'cow']
# print(type(tuple(list_b)))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#  Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# fam1 = input('Enter fam1 members separated by commas: ' ).split(',')
# fam2 = input('Enter fam2 members separated by commas: ' ).split(',')
#
# if len(fam1) > len(fam2):
#     print(fam1)
# elif len(fam1) < len(fam2):
#     print(fam2)
# else:
#     print('equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# myFilm ={
#     "title": "Mysoul",
#     "director": "Santa Monica",
#     "year": "2019",
#     "budget": "100 000 000",
#     "main_actor": "LilianNik",
#     "slogan": "Happiness is where we are!"
#}
#  3.5.1
# for item in myFilm.items():
#     key, value = item
#     print(item)
#     print(key)
#     print(value)
# myFilm ={
#     "title": "Mysoul",
#     "director": "Santa Monica",
#     "year": "2019",
#     "budget": "100 000 000",
#     "main_actor": "LilianNik",
#     "slogan": "Happiness is where we are!"
# }
# for value in myFilm.values():
#     print(value)
#  3.5.2
# myFilm ={
#     "title": "Mysoul",
#     "director": "Santa Monica",
#     "year": "2019",
#     "budget": "100 000 000",
#     "main_actor": "LilianNik",
#     "slogan": "Happiness is where we are!"
# }
# # for keys in myFilm.keys():
# #     print(keys)
#
# for key,value in myFilm.items():
#     print(f"{key}: {value}")


#  3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum_digits = sum(my_dictionary.values())
# print(sum_digits)

#  3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# my_list3 = [1, 2, 3, 4, 5, 3, 2, 1]
# new_list = list(set(my_list3))
# print(new_list)
#  3.7
# def list_to_set(T_list):
#     my_set = set(T_list)
#     return my_set
#
# print(list_to_set(new_list))
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# res = 0
# for x in my_dictionary:
#     res += my_dictionary[x]
#print(res)

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# common = set1&set2
# print(common)

print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))
