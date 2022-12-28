

# import lec as l
# print(l.f(1))

def concatenatio (*params):
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))
print(concatenatio('a', '1'))