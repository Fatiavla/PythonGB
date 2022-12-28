# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# x = float(input('Введите число: '))

# if x - int(x) == 0:
#     print('No')
# else:
#     print(f'{x-int(x)}')


from decimal import Decimal
number = float(input('Введите число: '))
if number % 1 == 0:
    print('No')
else:
    print(int(number * 10 % 10))


numbers = input('Введите число: ')
numbers = numbers.split('.')
if len(numbers) > 1:
    print(numbers[1][0])
else:
    print('Число целое')


# Работа с плавающей точкой

number_new = Decimal('0.56')
print(number_new * 10)
