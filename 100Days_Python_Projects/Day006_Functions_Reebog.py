# Functions

def my_function():
    print('Hello')
    print('Bye')


my_function()

# Reebog project


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
