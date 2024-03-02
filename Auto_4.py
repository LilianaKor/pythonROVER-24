# 4.1  Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# a = int(input('Enter the square side'))
# print((a*a, a*4, round(a * (2 ** 0.5))))
#from functools import reduce

# 4.2 Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# my_dict = {
# 'name': "John",
# 'last_name': "Smith",
# 'age': 35,
# 'position': "web developer"}
# #print(my_dict)
# def print_key_values(**kwargs):
#     #print(*kwargs, sep='\n')
#     # for key in kwargs:
#     #     print(kwargs[key])
#     print(*kwargs.items(), sep='\n')
# print_key_values(name='John', last_name= 'Smith', age= 35)

# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# employee(last_name='Popov', name='Max', age=40, position='web developer')

#4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     # положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)

# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)

# from functools import reduce
#
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)
# res = reduce(lambda x, y: x * y, new_list)
#
# print(res)

# Чтобы получить результат перемножения только положительных значений
#print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
#import time

# def calculate_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Execution time of {func.__name__}: {execution_time} seconds")
#         return result
#     return wrapper

 # Пример использования декоратора
# @calculate_execution_time
# def example_function():
#     time.sleep(2)
#     print("Function executed")

#example_function()

# 4.6  my_calc.py

# def add(x, y):
#     """Сложение двух чисел."""
#     return x + y
#
# def subtract(x, y):
#     """Вычитание одного числа из другого."""
#     return x - y
#
# def multiply(x, y):
#     """Умножение двух чисел."""
#     return x * y
#
# def divide(x, y):
#     """Деление одного числа на другое."""
#     if y == 0:
#         return "Ошибка: деление на ноль!"
#     return x / y
#
# # main.py
#
# from my_calc import add, subtract, multiply, divide
#
# # Вызов функций как методов
# print("Сложение:", add(5, 3))
# print("Вычитание:", subtract(10, 4))
# print("Умножение:", multiply(6, 7))
# print("Деление:", divide(15, 3))


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
#4.6.2. - it's working
# def sum(a,b):
#     return a + b
#
# def subtract(a,b):
#     return a - b
#
# def multiply(a,b):
#     return a * b
#
# def devide(a,b):
#     return a / b
# from my_calc import *
# print(sum(10,2))
# print(subtract(10,2))
# print(devide(10,2))
# print(multiply(10,2))

#4.6  my_calc.py - ex. Aigul
def add(x, y):
    return x + y
def remain(x, y):
    return x % y
def subtract(x, y):
    return x - y
def prod(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"


from my_file import *
prod_res = prod(100, 20)
print(prod_res)
div_res1 = divide(45, 9)
print(div_res1)
div_res2 = divide(5, 0)
print(div_res2)
add_res = add(585, 1987)
print(add_res)
remain_res = remain(541, 6)
print(remain_res)
sub_res = subtract(230, 149)
print(sub_res)