# builidng my fav snake game finally. 18/11/23



from turtle import Screen, Turtle
from Sna import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Red")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()