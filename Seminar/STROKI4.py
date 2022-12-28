my_string = 'Питон самый лучший в мире язык'
my_string2 = '     \tПитон самый лучший в мире язык\n'
my_list = ['21', '333', '444', 'qweqw', 'eee']

add = '-'
print(add.join(my_list)) # join склеивает списки

new_string = my_string.split()

new_string2 = my_string.replace('и', '$').replace('П', '!')

new_string3 = my_string2.strip() # Очищает строку от пробелов 



if my_string.startswith('Пит'):
    print('Да, все верно')

if my_string.endswith('зык'):
    print('Да, все верно')

if my_string.lower().startswith('пит'):
    print('Да, все верно')

if my_string.upper().startswith('ПИТ'):
    print('Да, все верно')

print(new_string)
print(new_string2)
print(new_string3)