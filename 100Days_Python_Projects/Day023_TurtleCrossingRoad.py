import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreborad = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.restart, 'space')

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreborad.game_over()
            game_is_on = False

    if player.finish_line():
        player.restart()
        car_manager.level_up()
        scoreborad.increase_score()


screen.exitonclick()
# Turtle crossing road, rest in OOP folder
