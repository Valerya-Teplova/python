#Словарь цветов.

print("Вас приветствует словарь цветов")


rgbTuple =('0, 0, 0', '255, 255, 255', '255, 0, 255', '128, 0, 128',
 '255, 0, 0', '255, 255, 0', '0, 255, 0', '0, 0, 255')
Color =('Black', 'White', 'Fuchsia', 'Purple', 'Red', 'Yellow', 'Lime', 'Blue')
ColorBook = dict(zip(Color, rgbTuple))
print(ColorBook)

