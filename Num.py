"""
Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.
"""

def num():
    while True:
        try:
            Number1 = int(input("Введите число 1: "))
            Number2 = int(input("Введите число 2: "))
            sum = Number1 + Number2
            print('Сумма чисел: ', sum)
            break
        except ValueError:
            print('Вы вели не число. Попробуйте снова')

num()