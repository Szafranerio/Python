# Snake project

from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)

x_position = [0, -20, -40]
segments = []

for snake in range (0,3):
    all_snakes = Turtle(shape='square')
    all_snakes.color('white')
    all_snakes.penup()
    all_snakes.goto(x=x_position[snake], y=0)
    
    segments.append(all_snakes)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
        

screen.exitonclick()