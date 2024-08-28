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
colors = ['purple', 'red', 'yellow', 'blue', 'orange', 'green']
y_positions = [-70, -40, -10, 20, 50, 80]

turtles = []

def get_colors():
    return random.choice(colors)

for turtle_index in range(len(colors)):
    all_turtles=Turtle('turtle')
    all_turtles.color(colors[turtle_index])
    all_turtles.penup()
    all_turtles.goto(x=-230, y = y_positions[turtle_index])    
    turtles.append(all_turtles)
    
if user_bet :
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:   
                print(f'Congrats, your {user_bet} turtle has won!')
            else:
                print(f'{winning_color.capitalize()}, has won')
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()