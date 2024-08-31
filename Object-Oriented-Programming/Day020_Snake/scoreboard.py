from turtle import Turtle

# Corrected variable name
POSITION = [0, 260]
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        
        # Handle file not found scenario
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
            with open("data.txt", mode='w') as data:
                data.write("0")
        
        self.penup()
        self.color('white')
        self.goto(POSITION)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High score is {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
         
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # No need to clear again, `update_scoreboard` already does it
