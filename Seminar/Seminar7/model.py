# база данных где храним всю инфу и тут же будут все функции. Только книгу и методы работы с ней
import re

phone_book = []
path = 'Seminar\Seminar7\phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding ='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    print(phone_book)

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)



def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding ='UTF-8') as data:
        data.write('\n'.join(pb_str))

def del_contacts ():
    global phone_book
    i = int(input('Введите номер, который хотите удалить: '))
    phone_book.pop(i-1)


    

