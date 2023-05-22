# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))
if 100 <= number <=999:
    sum = 0
    while number > 0:
        sum = sum + (number % 10)
        number = number // 10
    print(F'Сумма цифр цисла {number} = {sum}')
else:
    print("Введено не трехзначное число!!!")
