# my_file.py
from my_calc import *

prod_res = multiply(100, 20)
print("Product:", prod_res)

try:
    div_res1 = divide(45, 9)
    print("Division 1:", div_res1)
except ValueError as e:
    print("Error:", e)

try:
    div_res2 = divide(5, 0)
    print("Division 2:", div_res2)
except ValueError as e:
    print("Error:", e)

add_res = add(585, 1987)
print("Addition:", add_res)

remain_res = mod(541, 6)  # Assuming you have a function named `mod` for finding remainder
print("Remainder:", remain_res)

sub_res = subtract(230, 149)
print("Subtraction:", sub_res)
