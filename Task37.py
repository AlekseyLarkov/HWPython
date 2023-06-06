# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def Fill_string(numb):
    str_a = str()
    if numb == 1:
        str_a += str(input('Введите значение элемента:'))
        return str_a
    else:
        str_a += str(input('Введите значение элемента:')) + Fill_string(numb - 1)
        return str_a

def Print_expand_string(str_a):
    if len(str_a) == 1:
        print(str_a)
    else:
        print

n = int(input('Введите число: '))
string_a = Fill_string(n)
print(string_a)
    
