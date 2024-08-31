#US state game

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S State Game')

#Path
image = "/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day025_US_StateGame/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('/Users/bartlomiejszafran/Desktop/GitHub/Python/100Days_Python_Projects/data/Day025_US_StateGame/50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the state', prompt='Enter the name of the state').title()

    if answer_state == 'Exit':
        missing_states= []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        
