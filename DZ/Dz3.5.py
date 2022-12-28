# Числа фибоначи

# f1 = 1
# f2 = 1
# n = int(input())
# fib1=[]
# print(f1, f2, end=' ')
# for i in range(2, n):
#     f1, f2 = f2, f1 + f2
#     print(f2, end =' ')

# print()

# f3 = 1
# f4 = -1
# z = int(input())
# fib2 = []
# print(f3, f4, end=' ')
# for i in range(2, z):
#     f3, f4 = f4, f3 - f4
#     print(f4, end =' ')

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def fibonacci2(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b

data = list(fibonacci(8))
data2 = list(fibonacci2(8))
print(data)
# print(data2)

new_data2 = list(reversed(data2))
print(new_data2+[0]+data)