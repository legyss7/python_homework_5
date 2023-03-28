# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number_a = int(input('Введите основание степени: '))
number_b = int(input('Введите показатель степени: '))

def pow_number(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pow_number(a, b-1)


print(f'{number_a} в {number_b} степени равно {pow_number(number_a, number_b)}')