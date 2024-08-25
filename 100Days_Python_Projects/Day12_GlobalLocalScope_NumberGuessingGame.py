#Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
#Not defined, becasue var is defined only in a function and works only for that function!!!
#print(potion_strength)


#Global scope, var is defined before funtion so I can use it anytime 
player_health = 10 

def drink_potion():
    potion_strength = 2
    print(player_health)
    
drink_potion()


def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

is_prime(45)

#Guessing the number games
import random

print('Hello in the number guess generator')
print('Im choosing the number please wait?...')
number = random.randrange(0,100)

difficulty = ''
while difficulty not in['e', 'h']:
    difficulty = input("Please choose difficulty. e for easy, h for hard")

lives = 10 if difficulty =='e' else 5
print(f'You have choosen {difficulty}, you have {lives} chances')

game_over = False
used_numbers = []

while not game_over:
    guess = int(input('What is the number? '))
    if guess < number:
        print('Too low')
        if guess != number:
            lives -=1
            used_numbers.append(guess)
            print(f'You have {lives} left')
            print(f'You have used those numbers {used_numbers}')
    elif guess > number:
        print('Too high')
        if guess != number:
            lives -=1
            used_numbers.append(guess)
            print(f'You have {lives} left')
            print(f'You have used those numbers {used_numbers}')
    if lives == 0:
                print('You lost')
                game_over = True 
    elif guess == number:
            game_over = True
            print(f'You guessed a {number}, you won!!!')