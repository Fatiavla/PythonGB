#  Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
string = '1-2*3'
new_string = string.replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').split()
while len(new_string) > 1:
    i = 0
    while '*' in new_string or '/' in new_string:
        while i < len(new_string):
            if new_string[i] == '*':
                new_string [i-1] = int(new_string[i-1]) * int(new_string[i+1])
                new_string.pop(i)
                new_string.pop(i)

            elif new_string[i] == '/':
                new_string [i-1] = int(new_string[i-1]) / int(new_string[i+1])
                new_string.pop(i)
                new_string.pop(i)

while len(new_string) > 1:
    i = 0
    while '+' in new_string or '-' in new_string:
        while i < len(new_string):
            if new_string[i] == '+':
                new_string [i-1] = int(new_string[i-1]) + int(new_string[i+1])
                new_string.pop(i)
                new_string.pop(i)

            elif new_string[i] == '-':
                new_string [i-1] = int(new_string[i-1]) - int(new_string[i+1])
                new_string.pop(i)
                new_string.pop(i)

# print(words) 
print(new_string)

# for x in range(len(new_string)):
#     if new_string[x] == int:
#         words += new_string[x]
# print(new_string[x])