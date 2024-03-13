lst = [1, 3, 5, 6, 7, 8 ,9]

def add_two(x):
    return x + 2

sum_2 = list(map(add_two, lst))
print(sum_2)
#print(*sum_2, sep='\n')
print(*sum_2, sep='\n')
