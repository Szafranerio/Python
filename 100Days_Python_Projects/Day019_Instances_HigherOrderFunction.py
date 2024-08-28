from turtle import Turtle, Screen
import random

#tim = Turtle()
#screen = Screen()

#Sketch project
#def move_forward():
#    tim.forward(10)
#    
#def move_back():
#    tim.back(10)
#    
#def rotate():
#    tim.right(45)
#    
#def rotate_back():
#    tim.left(45)
#    
#def circle():
#    tim.circle(50)
#    
#screen.listen()
#screen.onkey(move_forward, "w")
#screen.onkey(move_back, "s")
#screen.onkey(rotate, "d")
#screen.onkey(rotate_back, "a")
#screen.onkey(circle, "o")
#screen.exitonclick()


#Turtle race!!!
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title='Make your bet', prompt='Enter the color: ')
colors = ['purple', 'red', 'yel