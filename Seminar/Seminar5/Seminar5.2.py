# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его

# data = open('file.txt', 'a')
# # data.writelines(colors)
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

# with open ('file.txt', 'a') as data:
#     data.write('line 111\n')
#     data.write('line 2222\n')


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close

# exit()

path = 'file.txt'
data = open(path, 'r')
data_read = data.read()
data_read = list(map(int, data_read.split()))
print(data_read)

# numbers = [(i, item) for i, item in enumerate (data_read)]
# new_numbers = list(filter(lambda i, item: item != i+1, numbers))
# print(numbers)
# print(new_numbers)



data_read =[data_read[x]-1 for x in range(1, len(data_read)) if data_read[x] - 1 != data_read[x-1]]
print(data_read)