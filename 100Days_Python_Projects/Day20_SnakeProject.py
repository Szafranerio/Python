# Snake project

from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)

x_position = [0, -20, -40]

for snake in range (0,3):
    all_snakes = Turtle(shape='square')
    all_snakes.color('white')
    all_snakes.goto(x=x_position[snake], y=0)
    all_snakes.penup()

screen.exitonclick()