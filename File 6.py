# движение персонажа по координатной оси. начальная позиция (0,0)


import turtle
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PROJECTILE_SPEED = 3

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.goto(0,0)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

moving = str(input("Введите направление( влево, вправо, вверх, вниз): "))
V = "вверх"
v = "вниз"
L = "влево"
R = "вправо"

def mov():
    if moving == V:
        turtle.goto(0,90)
    elif moving == v:
        turtle.goto(0, -90)
    elif moving == L:
        turtle.goto(-90,0)
    elif moving == R:
        turtle.goto(90,0)
    else: print("err")
mov()




