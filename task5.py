"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit

print(timeit("""
def my_func_sort(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    a.sort(reverse=True)
    print(a[0] + a[1])
""", number=100000))

print(timeit("""
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
""", number=100000))

# Результат: В данном случае использование функции sort() замедляет выполнение кода