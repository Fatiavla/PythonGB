

def split_numbers(string: str):
    new_numbers = string.replace(
        '-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').split()
    return new_numbers


def solution(new_string: list):
    while len(new_string) > 1:
        while '*' in new_string or '/' in new_string:
            i = 0
            while i < len(new_string):
                if new_string[i] == '*':
                    new_string [i-1] = int(new_string[i-1]) * int(new_string[i+1])
                    new_string.pop(i)
                    new_string.pop(i)

                elif new_string[i] == '/':
                    new_string [i-1] = int(new_string[i-1]) / int(new_string[i+1])
                    new_string.pop(i)
                    new_string.pop(i)
                i += 1       
        while '+' in new_string or '-' in new_string:
            i = 0
            while i < len(new_string):
                if new_string[i] == '+':
                    new_string [i-1] = int(new_string[i-1]) + int(new_string[i+1])
                    new_string.pop(i)
                    new_string.pop(i)

                elif new_string[i] == '-':
                    new_string [i-1] = int(new_string[i-1]) - int(new_string[i+1])
                    new_string.pop(i)
                    new_string.pop(i)
                i+= 1
    return new_string[0]

