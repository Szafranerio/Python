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
screen.onkey(player.go_down, "Down