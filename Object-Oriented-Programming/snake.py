from turtle import Turtle
START = [0, -20, -40]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for snake in range(0, 3):
            all_snakes = Turtle(shape='square')
            all_snakes.color('white')
            all_snakes.penup()
            all_snakes.goto(x=START[snake], y=0)
            self.segments.append(all_snakes)
            
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)