# Вводится радиус круга.
#Расчитать площадь круга

radius = int(input('Введите радиус: '))
const = 3.14
if radius >=0:
    k = const * radius ** 2
    print("Площадь круга: ",k)
else:
    print("Введите положительное число!")
