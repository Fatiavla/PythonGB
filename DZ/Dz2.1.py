# Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


number = float(input('Введите число: '))

result = 0
for i in str(number):
    if i != '.':
        result += int(i)


print(result)

#Второй Вариант с добавлением map ( семинар 6)

def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')
