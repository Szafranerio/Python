import random

sex_positions = []
times = [1, 5, 10, 15, 20, 35, 50]

game_on = True

while game_on:
    x = input("Enter the position, write 'end' to draw a postion: ").capitalize()
    if x == 'End':
        game_on = False
        print(f' Your libary is {sex_positions}')
    else:
        sex_positions.append(x)
        position = random.choice(sex_positions)

time = random.choice(times)
print(f'Choosen position is {position}')
print(f'Your time is {time} minutes')
