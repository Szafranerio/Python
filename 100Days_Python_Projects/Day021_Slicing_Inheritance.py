# Snake project cont....

# Class Inheritance

class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print('Inhale, exhale')


leo = Animal()
leo.breathe()

# You can create main class with the main functionallity and later create sub-class that will have own
# but can take some atributes from the main class. You can also modify it in the subclass.."""


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('Under water')

    def swim(self):
        print('Swim swim')


nemo = Fish()
nemo.swim()
nemo.breathe()

#Whole code snake game, rest in OOP folder
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from obstacles import Obstacels

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True

decision = screen.textinput("Rules", "Welcome, collect blue points to extend the snake and avoid red. If you collect red point, game is over! Type 'off' to quit")
if decision == 'off':
    game_is_on = False



snake = Snake()
food = Food()
scoreboard = Scoreboard()
obstacles = Obstacels()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh() 
        obstacles.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.distance(obstacles) < 15:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()

