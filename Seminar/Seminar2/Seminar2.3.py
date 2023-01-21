# 1. Напишите программу, которая принимает на 
# вход число N и выдаёт последовательность из N членов.   
# *Пример:*  
#  - Для N = 5: 1, -3, 9, -27, 81

# 221  333 444 55555

# 5 = 12 15 -23 -5 12

# number = int(input('Введите число: '))
# num = []
# import random
# for i in range(number):
#     n = random.randint(1, 100)
#     num.append(n)

# print(num)


number = int(input('Введите число: '))
my_list = []
for i in range(number):
   my_list.append((-3)**i)

print(*my_list, sep = ', ')
