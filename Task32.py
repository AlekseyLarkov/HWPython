# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def Fill_list(some_list, num):
    for _ in range(num):
        some_list.append(random.randint(1, 31))
    return some_list

def Check_list(some_list, max, min):
    result = list()
    for i in range(len(some_list)):
        if min <= some_list[i] <= max:
            result.append(i)
    return result


n = int(input('Введите количество элементов в списке: '))
max_d = int(input('Введите значение максимума: '))
min_d = int(input('Введите значение минимума: '))
list_number = list()
list_number = Fill_list(list_number, n)
print(f'Заданный список: {list_number}')
list_index = Check_list(list_number, max_d, min_d)
print(f'Индексы значений - {list_index} лежащих в диапазоне от {min_d} до {max_d}')
