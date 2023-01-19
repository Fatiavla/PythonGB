# # print('hello world')
# # ('int, float, boolean, str list')  # ЭТО ПЕРЕМЕННЫЕ None (можно присвоить своей переменной, что бы потом ее использовать)

# # ТИПЫ ДАННЫХ!!!!!!!!!!!!!!!

# # value = None
# # print(type(value))
# # a = 123
# # b = 1.23
# # print(type(a)) # type - для того, что бы узнать какой это тип данных
# # print(type(b))
# # value = 12334
# # print(type(value))
# # s = 'hello world' # \n перенос на новую строку

# # print(s) # вывод строки
# # print(a, '-', b, '-', s)
# # print('{} - {} - {}'.format(a,b,s)) # тоже самое что и сверху
# # print(f'{a} - {b} - {s}') # тоже самое что и сверху
# # print('{1} - {2} - {0}'.format(a,b,s)) # поменять местами по массиву (индексу)

# # f = False
# # print(f)
 
# # list = [] # Массив (объявление)
# # print(list)
# # list = [1,2,3]
# # print(list)
# # list = ['1','2','3', 'hello', 1,2,4.5, True]
# # print(list)
# # col = ['hello', 1,2,4.5, True]
# # print(col)

# # ВВОД ДАННЫХ!!!!!!!!!!!!!

# # print('Введите a')
# # a = int(input()) # что бы получить строку, убрать int
# # print('Введите b')
# # b= int(input()) # что бы получить веществ. знач используем float
# # print(a,'+' ,b,'=', a+b)

# # +, -, *, /, %, //, **
# # приоритет операвций **,
# # () скобки меняют приоритет

# a = 123 # добавил унарный плюс 
# b = -321 # добавил унарный минус (т.е теперь 123 + (-321) = - 198)
# c = a+b
# print (c)
# #вычитание
# a = 2 
# b = 8 
# c = a-b
# print (c)
# #умножение
# a = 2 
# b = 8 
# c = a*b
# print (c)
# # Деление
# a = 12 
# b = 8 
# c = a/b
# print (c)

# # Деление для получения целого числа
# a = 12 
# b = 5 
# c = a//b # используем еще один /
# print (c)

# # Остаток от Деления
# a = 12 
# b = 8 
# c = a%b 
# print (c)

# # Возведение в степень 
# a = 2 
# b = 8 
# c = a**b # добавляем еще одну *
# print (c)

# # Округление
# a = 1.3 
# b = 3 
# c = round(a*b, 5) # округление по мат правилам (5 - кол-во знаков после запятой)
# print (c)

# #Сокращенные операции присваивания
# a = 3
# # a = a + 5
# a += 5
# print(a)


# # ЛОГИЧЕСКИЕ ОПЕРАЦИИ!!!!!!!!!!
# # >, >=, <, <=, ==, !=
# # not, and, or = не путать с &, |, ^
# # Кое что еще: is, is not, in, not in

# # Больше 
# a = 1>4
# print(a)

# # Меньше
# a = 1<4
# print(a)

# # несколько операций для проверки
# a = 1<4 and 5 > 2
# print(a)

# # Сравнение строк
# a = 'qwe'
# b = 'qwe'
# print(a == b)

# # Сравнение списков (массива)
# a = [1,2]
# b = [1,2]
# print(a == b)

# # Использования тройного неравенства
# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>x)

# # логическая операция
# f = 1 > 2 or 4 < 6
# print(f)

# # Список с in
# f = [1,2,3,4]
# print(f)
# print(2 in f) # Отрицание - добавление not

# # проверка факта четности числа
# is_odd = f[0] % 2 == 0
# print(is_odd)

# # Упарвляющая конструкция if if - else

# a = int (input('a ='))
# b = int (input('b ='))
# if a > b:
#     print(a)
# else:
#     print(b)

# # If в связке elIf

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША')
# elif username == 'Марина':
#     print('Я так ждал вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# # WHILE (ЦИКЛ)

# original =23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# # У цикла While есть else

# original =23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)

# # Цикл For

# for i in 1,2,3,4,5:
#     print(i**2)

# # Список
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# # Использование Range от 0 до n где N - range (N)
# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)
# for i in range(1, 5):
#     print(i)
# for i in range(1, 10, 2):
#     print(i)
# for i in 'qwerty':
#     print(i)

# # Немного о строках
# text = 'съешь еще этих мягких французких булок'

# help(text.istitle) # Если не знаешь, что делает команда, использовать help


# print(len(text)) #39
# print('еще' in text) #true
# print(text.isdigit()) #false (символы верхнего регистора)
# print(text.islower()) #true (символы нижнего регистора)
# print(text.replace('еще', 'ЕЩЁ')) #

# for c in text:
#     print(c)


# text = 'съешь еще этих мягких французcких булок'
# print(text[0])                  # c
# print(text[1])                  # Ъ
# print(text[len(text)-1])        # к
# print(text[-5])                 # б
# print(text[:])                  # съешь еще этих мягких французcких булок
# print(text[2:5])                # съ
# print(text[len(text)-2:])       # ок
# print(text[2:9])                # ешь еще
# print(text[6:-18])              # еще этих мягких
# print(text[0:len(text):6])      # сеикал
# print(text[::6])                 # сеикал
# text = text [2:9] + text[-5] + text[:2] # ...

# # Список: введене
# ## list = list

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)
# for e in colors:
#     print(e*2)

# colors.append('gray') #Добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'] ) #true
# colors.remove('red') #del colors [0] #Удалить элемент


def f(x):
    if x == 1:
        return 'Целое'
    elif x ==2.3:
        return 23
    else:
        return

arg =1 
print(f(arg))
print(type(f(arg)))