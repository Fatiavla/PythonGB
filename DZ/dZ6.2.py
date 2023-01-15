# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
# Задание 2.2

#Enumirate + list compl

n = int(input('Введите число последовательности: '))
def answer (n):
    return [round((1 + 1 / i)** i , 3)  for i in range(1, n+1)]
new_list = list(enumerate(answer(n)))
print(f'Последовательность: {new_list}\nСумма: {round(sum(answer(n)), 2)}')