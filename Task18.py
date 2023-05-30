# Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите количество элементов в списке: '))
x = int(input('Введите некоторое число Х: '))
list_a = []
for _ in range(n):
    list_a.append(int(input('Введите элемент списка(Целое число): ')))
min_diff = x
min_ind = 0
for i in range(len(list_a)):
    buf = x
    if buf > list_a[i]:
        j = int(0)
        while buf > list_a[i]:
            buf -= 1
            j += 1
        if j < min_diff:
            min_diff = j
            min_ind = i
    else:
        j = int(0)
        while buf < list_a[i]:
            buf += 1
            j += 1
        if j < min_diff:
            min_diff = j
            min_ind = i
print(f'Ближайшее число в списке = {list_a[min_ind]}')


    
    