"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

def my_div(arg1, arg2):
    return arg1 / arg2

arg1 = int(input("Введите первое число : "))
arg2 = int(input("Введите второе число : "))

if arg2 == 0:
    print('Вы что? Пытаетесь делить на 0!')
    quit()
else:
    print(my_div(arg1, arg2))