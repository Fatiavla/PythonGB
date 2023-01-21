# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
c = int(input('Введите 3 число '))
d = int(input('Введите 4 число '))
f = int(input('Введите 5 число '))


mas = [a, b, c, d, f]
max = mas [0]
for i in mas:
    if i > max:
        max = i
        
print(max)
        
my_list = [4,6,8,2,0,9]
for i in range(5):
    print(my_list[i])

my_list = [4,6,8,2,0,9]
for i in range(len(my_list)):
    print(my_list[i])

my_list = [4,6,8,2,0,9]
for i in my_list:
    print(i)


# РЕШЕНИЕ

my_list = []

for i in range(5):
    number = int(input(f'Введите  {i+1} число: '))
    my_list.append(number) # Добавляет элементы в список (массив)

max = my_list[0]

for item in my_list:
    if item > max:
        max = item

print(f'В данном списке максимальное число - {max}')

