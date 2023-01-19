# [exp for item in iterable]
# [exp for item in iterable ( if conditional)]

# list = []

# for i in range (1, 101):
#     if i%2 == 0:
#         list.append(i)
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range (1,21) if i%2 == 0]
# print(list)



# def mylt (y):
#     return y ** 2
# new_list1 = [1,2,3,5,8,15,23,38]
# new_list = [(z, mylt (z)) for z in new_list1 if z % 2 == 0]
# print(new_list)

def select (f , col):
    return [f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x:(x, x**2), res)
print(res)