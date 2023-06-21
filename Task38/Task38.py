# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.


def Search_phonebook():
    print('Как вы хотите искать?')
    mod1 = int(input('1 - по человеку, 2 - по № телефона: '))
    with open('E:\Новая папка\Git\HWPython\Task38\phonebook.txt', 'r', encoding='utf-8') as f_read:
        book = f_read.read().splitlines()
        if mod1 == 1:
            human = input('Введите фамилию, имя или отчество: ')
            for person in book:
                some_man = person.split(':')
                buf = some_man[0]
                if buf == human:
                    print(person)
                else:
                    name = buf.split()
                    for partname in name:
                        if partname == human:
                            print('Человек которого вы искали')
                            print(person)
        elif mod1 == 2:
            num = input('Введите номер телефона: ')
            for person in book:
                some_man = person.split(':')
                number = str(some_man[1])
                number = number[1:]
                if number == num:
                    print('Человек которого вы искали')
                    print(person)
        else:
            print('Некорректный режим!')

def Entry_phonebook():
    with open('E:\Новая папка\Git\HWPython\Task38\phonebook.txt', 'a', encoding='utf-8') as f_entry:
        print('Введите нового абонента:')
        name = input('Введите Ф.И.О: ')
        number = input('Введите номер телефона: ')
        f_entry.writelines('\n')
        f_entry.writelines(f'{name}: {number}')

def Change_phonebook():
    print('Что вы хотите изменить?')
    mod1 = int(input('1 - человека, 2 - № телефона: '))
    with open('E:\Новая папка\Git\HWPython\Task38\phonebook.txt', 'r', encoding='utf-8') as f_change:
        book = f_change.read().splitlines()
        book = list(book)
        human = input('Введите фамилию, имя или отчество: ')
        for person in book:
            some_man = person.split(':')
            buf = some_man[0]
            number = str(some_man[1])
            if buf == human:
                if mod1 == 1:
                    new_man = input('Введите новое Ф.И.О: ')
                    person = new_man + ': ' + number
            else:
                name = buf.split()
                for partname in name:
                    if partname == human:
                        if mod1 == 1:
                            new_man = input('Введите новое Ф.И.О: ')
                            book.remove(person)
                            person = new_man + ': ' + number
                            book.append(person)
        print(book)

print('Добро пожаловать в телефонный справочник!')
print('Выберите режим работы со справочником:')
mode = int(input('1 - чтение, 2 - запись, 3 - изменение: '))
if mode == 1:
    Search_phonebook()
elif mode == 2:
    Entry_phonebook()
elif mode == 3:
    Change_phonebook()
