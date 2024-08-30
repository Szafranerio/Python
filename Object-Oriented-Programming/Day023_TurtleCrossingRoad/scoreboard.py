from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-200, 270)
        self.write(f"Score: {self.score} ", align='center', font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align='center', font=FONT)
    
    def increase_scor