# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def Factorial(num_1, num_2):
    res = 1
    if num_2 == 1:
        res = res * num_1
        return res
    else:
        res = res * num_1 * Factorial(num_1, num_2 - 1)
        return res

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
factorial = Factorial(a, b)
print(f'Число {a} в степени {b} = {factorial}')
    