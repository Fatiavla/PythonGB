# def f(x):
#     return x**2

# g = f



# print(f(2))
# print(g(2))


# def calc1(x):
#     return x+10
# print(calc1(10))

# def calc2(x):
#     return x*10
# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)


# def sum(x, y):
#     return x+y


sum =  lambda x, y: x + y # тоже самое, что выше 

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a,b))
    # return op (a,b)

calc(lambda x, y: x + y, 5, 5)