dictionary = {}
dictionary = \
    {
        'up': '1',
        'left': '2',
        'down': '3',
        'right': '4',
    }
# print(dictionary)
# print(dictionary['left'])


for k in dictionary.keys(): # только ключи (левые)
    print(k)

for j in dictionary.values(): # только значения (правые)
    print(j)

for v in dictionary:
    print(v)

print(dictionary['up'])
dictionary['up'] = 'uup'
print(dictionary['up'])