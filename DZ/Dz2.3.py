# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int


import random
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

for i in range(len(my_list)):
    k = random.randint(0, 9)
    my_list[i], my_list[k] = my_list[k], my_list[i]

print(my_list)

