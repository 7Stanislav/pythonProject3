"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

# Решение с использованием функции sort()
def my_func_sort(*args):
    a = [*args]
    a.sort(reverse=True)
    print(a[0] + a[1])

my_func_sort(num1, num2, num3)


# Решение без использования функции sort()
def my_func(arg1, arg2, arg3):
    max_arg = arg1
    sec_arg = arg1
    if arg2 > max_arg:
        max_arg = arg2
        if arg1 > arg3:
            sec_arg = arg1
        else:
            sec_arg = arg3
    elif arg3 > max_arg:
        max_arg = arg3
        if arg1 > arg2:
            sec_arg = arg1
        else:
            sec_arg = arg2
    else:
        if arg2 > arg3:
            sec_arg = arg2
        else:
            sec_arg = arg3
    print(max_arg + sec_arg)

my_func(num1, num2, num3)