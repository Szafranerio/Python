STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
    def restart(self):
        restart = self.ycor(FINISH_LINE_Y)
        
