# creating hist painting using turtle module and importing pgb colors and randomly displaying them. 15/11/23



import turtle as tu
import random
tu.Turtle()

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

random_color = (random.choice(color_list))
tu.colormode(255)
tu.penup()
tu.speed("fastest")
tu.hideturtle()


def left_up():
    tu.setheading(90)
    tu.forward(50)
    tu.setheading(0)


def right_up():
    tu.setheading(90)
    tu.forward(50)
    tu.setheading(180)


for _ in range(5):
    for _ in range(10):
        tu.dot(20, (random.choice(color_list)))
        tu.setheading(180)
        tu.forward(50)
    left_up()
    for _ in range(10):
        tu.forward(50)
        tu.dot(20, (random.choice(color_list)))
    right_up()


screen = tu.Screen()
screen.exitonclick()