import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    
    
    
    if player.ycor() > 280:
        player.reset()
    
screen.exitonclick()
