# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
import random
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
for i in my_list:
    if my_list.count(i) == 1:
        print(i)



# Второе решение
my_list =[random.randint(0,10) for _ in range(15)]
print(my_list)
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)