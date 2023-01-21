import random
my_list = []
for i in range(10):
    my_list.append(i) #random.randint(0, 100)

print(my_list)
random.shuffle(my_list)
print(my_list)