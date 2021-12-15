"""
Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия).
""" 

def fib(n):
    cur = 1
    if n > 2:
        cur = fib(n-1) + fib(n-2)
    return cur

Fnum = int(input('Введите номер искомого элемента: '))
value = fib(Fnum)

print(str(Fnum) +' элемент последовательности равен ' + str(value))