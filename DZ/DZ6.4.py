import math
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# СЕМИНАР 3.2

#ZIP

list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))