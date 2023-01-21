# 1. проходимся по индексам, если индекс нечетный, то элемент добавляем к сумме
# 2. список берем 1 и последний, потом второй и предпоследний, если список нечетный, то тогда посредине останется один элемент, умнажаем само на себя
# 3. Задача (веществ - с дробной частью) Random.Uniform. 1.2 и 10.01 - берем числа после запятой
# 4.
# 5. Фибоначи - элемент сумма двух предыдущих элементов. Негафибоначи - эдемент разности двух предыдущих элементов.
# Мб сделать 2 списка, перевернуть и совместить ( из центра вправо и влево от 0) reverse, extend и тд


# Генерация Вещественных чисел
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

