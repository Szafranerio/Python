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
        self.restart()
        self.left(90)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
            
    def restart(self):
        self.goto(STARTING_POSITION)
        
