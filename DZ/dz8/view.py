
control = [ 'Элементарное сложение и вычитание (пример 1+1-1+1)',
            'Сложное уравнение (пример 1+2*2/1)',
            'Выход из программы']


def menu() -> int:
    print('Какой тип уравнения: ')
    for i, item in enumerate(control, 1):
        print(f'\t{i}.{item}')
    while True:
        try:
            choice = int(input('Выберете пункт меню: '))
            if 0 < choice < 4:
                return choice
            else:
                print('Введите значение от 1 до 3: ')
        except ValueError:
            print('Введите корректное значение: ')



def get_numbers(message: list):
    numbers = input(message)
    return numbers

def show_list(example):
    word = example
    print(word)

def end_program():
    print('До свидания! Программа завершена')