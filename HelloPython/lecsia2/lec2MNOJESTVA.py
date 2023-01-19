a = {1,2,3,4,5}
b = {3,5,7,8,9}
c = a.copy() # c = {1,2,3,4,5}
u = a.union(b) # u = {1,2,3,4,5,7,8,9}
i = a.intersection(b) # i = {3,5}
dl = a.difference(b) # dl ={1,2,4}
dr =b.difference(a) # dr = {7,8,9}

q = a \
    .union(b) \
        .difference(a.intersection(b))

s = frozenset(a)