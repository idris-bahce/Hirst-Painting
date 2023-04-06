from turtle import Turtle, Screen, colormode
import random


def random_color():
    color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

    x = random.choice(color_list)
    return x


colormode(255)
turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.backward(50 * 5)
turtle.right(90)
turtle.forward(50 * 5)
turtle.left(90)

row = 0
while row < 10:
    for i in range(10):
        turtle.dot(20, random_color())
        turtle.forward(50)
    turtle.backward(50 * 10)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    row += 1


screen = Screen()
screen.exitonclick()