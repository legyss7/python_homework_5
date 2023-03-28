# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

number_a = int(input('Введите положительное число А: '))
number_b = int(input('Введите положительное число Б: '))

# Вариант одни.
def sum_number(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_number(a+1, b-1)
print(f'Сумма А и Б равна {sum_number(number_a, number_b)}')

# Вариант два. Увеличивает быстродействие в случае если числа сильно отличаются. Например если 
# число А будет равно 200, а Б равно 1, то рекурсия будет вызвана 200 раз. Если поменять их местами.
# то всего один раз. 

# direction_flag = True
# if number_a < number_b:
#     direction_flag = False 

# def sum_number(a, b, direct):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         if direct == True:
#             return sum_number(a+1, b-1, direct)
#         else:
#             return sum_number(a-1, b+1, direct)
# print(f'Сумма А и Б равна {sum_number(number_a, number_b, direction_flag)}')


# Вариант три)))). Тоже что и вариант один, ток короче

# def sum_number(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return sum_number(a+1, b-1)
# if number_a > number_b:
#     print(f'Сумма А и Б равна {sum_number(number_a, number_b)}')
# else:
#     print(f'Сумма Б и А равна {sum_number(number_b, number_a)}')
