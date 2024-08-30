from turtle import Turtle

POSITION = [0, 260]
ALLIGMENT = 'center'
FONT = ('Arial', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align=ALLIGMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align=ALLIGMENT, font=FONT)
         
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
   
        
        
        
