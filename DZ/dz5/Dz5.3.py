# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

with open('dz5.3_RLE.txt', 'r') as data:
    my_text = data.read()

def encode(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode(my_text)
print(str_code)
dev_12 = str_code

with open('dz5.3_RLE_encod.txt', 'w') as data:
    data.write(dev_12)