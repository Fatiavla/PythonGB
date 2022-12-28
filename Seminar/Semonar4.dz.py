# 1. Вводим 9 - макс степень, много член идет от 9 и вниз. Сгенерировать цикл для многочленов, сгенерировать цикл
# вторая часть задания ( )

import random
k = int(input("Введите максимальную степень: "))
equation = {}
for i in range(k+1):
    equation[i] = random.randint(0,100)

print(equation)

eq_str = ''

for k,v in equation.items():
    if k == 1:
        eq_str+=f'{v}*x**x{k} +'
    elif k == 0:
        eq_str+=f'{v}+'
    else:
        eq_str += f'{v}*x**{k}+'
else:
    eq_str = eq_str[:-3]

print(eq_str)
equation1 = {4:6} # ключ - наша степень. 
equation2 = {4:5}
new_equation = {4:15}