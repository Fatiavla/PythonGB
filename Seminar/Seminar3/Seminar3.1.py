# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.


my_list = ['sadasdsdsad4tewt', 'asdad458', 'erwer579', '0the534']
print(my_list)


search = input('Введите искомое число: ')

for item in my_list:
    if search in item:
        print(f'Число {search} входит в заданный список')
        
else:
    print(f'Число {search} НЕ входит в заданный список')