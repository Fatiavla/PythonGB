#  Напишите программу, которая определит
# позицию второго вхождения строки в списке либо сообщит,
# что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(my_list)
# search = input('Введите искомое число: ')
# count = 0
# for i in range(len(my_list)):
#     if search == my_list[i]:
#         count +=1
#     if count == 2:
#         print(i)
#         break
# else:
#     print('-1')

my_list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list4 = ["123", "234", 123, "567"]


def check(my_list: list, search: str):
    count = 0
    for i in range(len(my_list)):
        if search == my_list[i]:
            count += 1
            if count == 2:
                print(f'Второй индекс вхождения {i}')
                break
    else:
        print('Второго вхождения нет')


check (my_list1, 'qwe')
check (my_list2, 'йцу')
check (my_list3, 'йцу')
check (my_list4, '123')