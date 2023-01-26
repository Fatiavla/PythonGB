import model
import view


def button_click():
    choice = ''
    while True:
        choice = view.menu()
        # print(choice)
        match choice:
            case 1:
                numbers = view.get_numbers('Введите уравнение: ')
                new_list = model.split_numbers(numbers)
                # view.check(new_list)
                print(new_list)
                for i in range(len(new_list)):
                    e = 0
                    if new_list[i] == '*' or new_list[i] == '/':
                        e = 1
                        print('Введите просто уравнение!')
                        break
                if e == 0:
                    get_sum = model.solution(new_list)
                    print(f'Сумма уравнения {numbers} = {get_sum}')
                else:
                    pass

            case 2:
                num = view.get_numbers('Введите уравнение: ')
                new_l = model.split_numbers(num)
                get_strong = model.solution(new_l)
                print(f'Сумма уравнения {num} = {get_strong}')
            case 3:
                view.end_program()
                break



    