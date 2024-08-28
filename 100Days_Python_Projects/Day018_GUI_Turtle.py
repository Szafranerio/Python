from turtle import Turtle, Screen
import random


#1. Challange straight line
#timmy = Turtle()
#timmy.shape('turtle')
#timmy.color('gold')
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#screen = Screen()
#screen.exitonclick()


#2. Challange dashed line

#tom = Turtle()
#tom.shape('turtle')
#tom.color('gold')
#
#for i in range(10):
#    tom.forward(10)
#    tom.penup()
#    tom.forward(10)
#    tom.pendown()
#
#screen = Screen()
#screen.exitonclick()

#3 CHallange figures

#bart = Turtle()
#bart.shape('turtle')
#bart.color('blue')
#
#def draw_figure(num_sides):
#    angle = 360 / num_sides
#    for n in range(num_sides):
#        bart.forward(100)
#        bart.right(angle)
#        
#for shape_side_n in range (3, 11):
#    draw_figure(shape_side_n)
#screen = Screen()
#screen.exitonclick()

#4. Challange Random Walk

#voyager = Turtle()
#voyager.shape('turtle')
#screen = Screen()
#screen.colormode(255)
#
#def color_more():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    random_color = (r, g, b)
#    return random_color
#
#directions = [0, 90, 180, 270]
#
#for _ in range(300):
#    voyager.color(color_more())
#    voyager.forward(50)
#    voyager.right(random.choice(directions))
#    voyager.speed(10)
#    voyager.pensize(5)
#    
#screen.exitonclick()

#5. Challange circle

dot = Turtle()
dot.shape('turtle')
screen = Screen()
screen.colormode(255)

def color_more():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,222)
    random_color = (r, g, b)
    return random_color

dot.speed('fastest')

def draw(size):
    for _ in range(int(360 / size)):
        dot.color(color_more())
        dot.circle(100)
        dot.setheading(dot.heading() + size)     
draw(5)
screen.exitonclick()