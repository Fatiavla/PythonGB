# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = [2, 3, 5, 9, 3]
answer = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        answer+=my_list[i]    
print(answer)

    