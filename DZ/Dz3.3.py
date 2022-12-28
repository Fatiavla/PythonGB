# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
my_list = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(10):
    amount = random.randint(0, 3)
    number = (round(random.uniform(0, 10), amount))
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)
print(my_list)
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []
for i in my_list:
    if i%1 != 0:
        i = round(i%1,2)
        new_list.append(float(i))
print(max(new_list) - min(new_list))