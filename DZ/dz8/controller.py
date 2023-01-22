import model
import view


def button_click():
    choice = ''
    while True:
        choice = view.menu()
        print(choice)
        match choice:
            case 1:
                numbers = view.get_numbers('Введите уравнение: ')
                new_list = model.split_numbers(numbers)
                get_sum = model.sum(new_list)
                print(f'Сумма уравнения {numbers} = {get_sum}')
            case 2:
                numbers = view.get_numbers('Введите уравнение: ')
                new_list = model.split_numbers(numbers)
                get_strong = model.sum(new_list)
                print(f'Сумма уравнения {numbers} = {get_sum}')
            case 3:
                view.end_program()
                break



    