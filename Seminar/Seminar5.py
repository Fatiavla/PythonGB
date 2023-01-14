from random import randint as RI


my_list = [x for x in range(10) if x % 2 != 1]
print(my_list)

my_list = [RI(0, 10) for x in range(10)]
print(my_list)

my_list = {x: x*2 for x in range(10)}
print(my_list)


my_list = [x for x in range(10)]
print(my_list)

# map применяет какую то функцию к каждому элементу
my_list = list(map(str, my_list))
print(my_list)


my_list = '23 4 5 6 78 987 45 23 4'
my_list = list(map(int, my_list.split()))
print(my_list)

my_list = '23 4 5 6 78 987 45 23 4'
my_list = list(filter(lambda x: '4' in x, my_list.split()))
print(my_list)

my_list = '23 4 5 6 78 987 45 23 4'
my_list = list(filter(lambda x: not '4' in x, my_list.split()))
print(my_list)


my_list = '23 4 5 6 78 987 45 23 4'
my_list = list(filter(lambda x: x % 2 == 0, list(
    map(int, my_list.split()))))  # filter фильтрует список
print(my_list)


my_list = '23 4 5 6 78 987 45 23 4'

my_list = my_list.split()
print(my_list)

for i, item in enumerate(my_list):  # enumirate нумерует список
    print(i, item)


my_list = '23 4 5 6 78 987 45 23 4'

my_list = my_list.split()
print(my_list)

for i, item in enumerate(my_list, 5):
    print(i, item)


my_list_1 = '23 4 5 6 78 987 45 23 4'.split()
my_list_2 = [124, 5, 342, 234, 3, 324, 123, 54, 2]
my_list_3 = ('sdas', 'asdasd', 6543, '43234', 312, '1231', 3, 5, '123')

print(list(zip(my_list_1, my_list_2, my_list_3)))  # ZIP склеивает списки


def power(x):
    if x%2 != 0:
        return x ** 2    # так lambda не сделает 
    else:
        return 1


lambda x : x**2  #lambda  - анонимная, однострочная функция, может принимать 2 аргумента, она должна что то возвращать 

func = lambda x : x**2
print(func(4))

def print_smile(name):
    print(f'{name}, Улыбнись')

on_click = lambda name: print_smile(name)