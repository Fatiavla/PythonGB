# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


# n = int(input('Введите число: '))
# my_list = []
# for i in range(1, 4):
#     my_list =[round((1 + 1/i)**i, 3)]
#     sumi = round(sum(my_list),3)
# print(my_list)

n = int(input('Введите число последовательности: '))
lst = 0
my_list = []
for i in range(1, n+1):
    lst = round((1+1/i)**i, 3)
    my_list.append(lst)

new_list = list(enumerate(my_list))
print(f'Последовательность: {new_list}\nСумма: {round(sum(my_list), 2)}')

