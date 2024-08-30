from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        level_count = 1
        self.update_score()
        
    def score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.level_count, align='center',
                   font=('Courier', 80, 'normal'))
    
    def next_level(self):
        self.level_score += 1
        self.score
    
        
    pass
