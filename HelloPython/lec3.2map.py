# li = [i for i in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data2 = map(int, input().split())

# for e in data2:
#     print(e)

# data2 = map('1 2 3 4 5 6'.split())

# for e in data2:
#     print(e)



data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)