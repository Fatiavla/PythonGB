my_dict = \
    {
        32:'32',
        3: 45,
        1: 'Один',
        'Ключ': 2134,
        'Cписок': [324,555,22,13]
    } # Парные элементы

my_dict['New'] = 'value'
my_dict[3] = my_dict.get(3) + 1

print(my_dict.get(2, '0'))
print(my_dict.get(1, '0'))
print(my_dict.get(2, 0) + my_dict.get(3, 0))
print(my_dict)




my_dict2 = {}

num_list = '2232134214152323512423565621312'

for dig in num_list:
    my_dict2[dig] = my_dict2.get(dig, 0) + 1

print(my_dict2)