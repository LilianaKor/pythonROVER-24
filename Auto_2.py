# x = 5
# print(x>5)

# x = 5
# print(x > 3 or x > 8)

# x = 5
# print(x < 3 or x > 8)
# x = 5
# print( not x > 3 )

# num = 5
# if num == 5:
#     print('Five!')
# else:
#     print("Not equal five")

# num = 6
# if num == 5:
#     print('Five!')
# else:
#     print("Not equal five")

# num = 9
# if num == 5:
#     print('Five!')
# elif num < 5:
#     print('Less then five')
# else:
#     print("More then five")

# print(2.1)
# num = 0
# if num  >= 1:
#     print('True')
# else:
#     print('False')

# num = 20
# if 10 < num < 100:
#     print('True')
# i = 0
# while i < 5:
#     i = i + 1
#     print(i)
#     if i == 3:
#        break

# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)

# i = 5
# while i > 0:
#     print(i, 'HELLO')
#     i = i - 1
# print( 'Go')

# 2.1.
health = int(input('Введите уровень здоровья вашего персонажа: '))

if health > 0:
    print('True')
else:
    print('False')

# 2.2  Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст
# “Четное”, а иначе - “Нечетное”

# number = int(input('Enter random number: '))
# if number % 2:
#     print('odd')
# else:
#     print('Even')

# 2.3 Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без
# остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также
# считается високосным (1200, 2000)

# def leap(year):
#     a = int(year) % 4
#     b = int(year) % 100
#     c = int(year) % 400
#     if (a == 0 and b == 0 and c == 0) or (a == 0 and b != 0):
#         print(a, b, c)
#         return "високосный"
#     else:
#         print(a, b, c)
#         return "не високосный"
#
# year = input("Введите год ")
# print(f'Год {leap(year)}')

# year = 2019
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(f'{year} is leap')
# else:
#     print(f'{year} is not leap')

# 2.4 Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# С циклом while
#
# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# i = 1
# while i <= num:
#     print(text)
#     i += 1

# С циклом for
# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)

# 2.5
# def calk():
#     num1 = int(input('Please enter number 1: '))
#     operator = (input('input an action operator: '))
#     num2 = int(input('Please enter number 2: '))
#
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = (num1 - num2)
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "**":
#         result = num1 ** num2
#     elif operator == "/":
#         if num2 != 0:
#             result = (num1 / num2)
#         else:
#            # result = "Cannot divide by 0"
#             print("Cannot divide by 0")
#             return None
#     elif operator == "//":
#         if num2 != 0:
#             result = (num1 // num2)
#         else:
#             print("Cannot divide by 0")
#             return None
#     else:
#         print("Incorrect operator entered")
#         return None
#     print(f"Result {num1}{operator}{num2} equals {result}")


# def calk():
#     num1 = int(input('Please enter number 1: '))
#     operator = input('Input an action operator: ')
#     num2 = int(input('Please enter number 2: '))
#
#     if operator in ["+", "-", "*", "**", "/", "//"]:
#         if operator == "+":
#             result = num1 + num2
#         elif operator == "-":
#             result = num1 - num2
#         elif operator == "*":
#             result = num1 * num2
#         elif operator == "**":
#             result = num1 ** num2
#         elif operator == "/":
#             if num2 != 0:
#                 result = (num1 / num2)
#             else:
#                 print("Cannot divide by 0")
#                 return None
#         elif operator == "//":
#             if num2 != 0:
#                 result = (num1 // num2)
#             else:
#                 print("Cannot divide by 0")
#                 return None
#
#         print(f"Result {num1} {operator} {num2} equals {result}")
#     else:
#         print("Incorrect operator entered")
#
# calk()

# 2.5. Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное
# арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
# import sys
# num1 = int(input('Пожалуйста, введите первое число: '))
# num2 = int(input('Пожалуйста, введите второе число: '))
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# result = 0
# if num2 == 0 and operator == '/':
#     # try:
#     result = num1 / num2
#     # except ZeroDivisionError:
#     #     print('На ноль делить нельзя!')
#     #     sys.exit()
# elif operator == '+':
#     result = num1 + num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')




