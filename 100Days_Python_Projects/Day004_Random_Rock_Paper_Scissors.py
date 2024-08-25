import random

random_int = random.randint(a=1, b=100)
print(random_int)

random_float = random.uniform(1, 10)
print(random_float)

coin = random.randint(1, 2)
if coin == 1:
    print("Heads")
else:
    print('Tails')


friends = ['David', 'Alice', 'Tom', 'Thomas']

# 1st solution
pay_the_bill = random.randint(0, 3)
if pay_the_bill == 0:
    print('David')
elif pay_the_bill == 1:
    print('Alice')
elif pay_the_bill == 2:
    print('Tom')
else:
    print('Thomas')

# 2nd solution
print(friends[pay_the_bill])

# 3rd solution
print(random.choice(friends))


fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])


# Rock, paper and scissors

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
game = [rock, paper, scissors]

print('Welcome to the rock, paper and scissors game')
player1 = int(input('Rock: 0, Paper 1, Scissors 2: '))
print(f'Players decided to choose: {game[player1]}')

computer = random.randint(0, 2)
print(f'Computer decided to choose: {game[computer]}')

if player1 == 0 and computer == 2:
    print('You win')
elif computer == 0 and player1 == 2:
    print('You lost')
elif player1 > computer:
    print('You win')
elif computer > player1:
    print('You lost')
elif player1 == computer:
    print('Draw')
else:
    print('You typed wrong number')
