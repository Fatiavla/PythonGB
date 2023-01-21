import math
'A*x**2 + B*x + C = 0'
'32*x**2 + 4*x - 6 = 0'


equation = '32*x**2 + 4*x - 6 = 0'


def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ', '').replace('=0', '').replace('+', ' ').\
        replace('-', ' -').split()
    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        elif item.startswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*x')[0]))
    return new_koef


create_koef(equation)


def solution(koef: list):
    a, b, c = koef
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b + math.sqrt(disc))/(2*a)
        x2 = (-b - math.sqrt(disc))/(2*a)
        return 2, round(x1, 2), round(x2,2)
    elif disc == 0:
        x = -b / (2 * a)
        return 1, round(x,2)
    else:
        return 0, None, None


print(solution(create_koef(equation)))
