print('Wlecome to the rollercoaster!')
height = int(input('WHat is your height? :'))

if height >= 120:
    print('You cannot buy a ticket')
    age = int(input('What is your age? '))
    if age <= 12:
        bill = 5
        print('Please pay 5$')
    elif age <= 18:
        print('Please pay 7$')
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print('It is your lucky day, free ride for you :)')
    else:
        bill = 12
        print('Please pay 12$')

    photo = input('Do you want a photo? y for Yes, n for No')
    if photo == 'y':
        bill = bill + 3

    print(f'Your final bill is {bill}')

else:
    print('You have to pay 10$')


print('Welcome to the odd, even check:')
number = int(input('Place your number: '))

if number % 2 == 0:
    print('This is even number')
else:
    print('This is odd number')


# Pizza order

print("Welcome to the pizza academy")
print('Small (S): $15, Medium (M): $20, Large (L): $25')
S = 15
M = 20
L = 25

size = input('Place your size order S,M or L: ')

if size == 'S':
    price = 15
    peperoni = input('Do you want peperoni? y for Yes n for No:')
    if peperoni == 'y':
        price += 2
elif size == 'M':
    price = 20
    peperoni = input('Do you want peperoni? y for Yes n for No:')
    if peperoni == 'y':
        price += 3
else:
    price = 25
    peperoni = input('Do you want peperoni? y for Yes n for No:')
    if peperoni == 'y':
        price += 3

    extra_cheese = input('Do you want extra cheese? y for Yes n for No:')
    if extra_cheese == 'y':
        price += 1

print(f'Your total {price}')


# Game Task

print('Welcome to the island of nothing')

beach = input('You are in the starting point on the rocky beach. Your mission is to find treasure. Where do you want to go? r for Right l for Left, s for straight: ')
if beach == 'r':
    print('You are in the woods, you found a cave do you want to go there?')
    cave = input('y for Yes, n for No: ')
    if cave == 'y':
        print('Good job you are almost there')
        print('You found a chest, but first you have to solve that:')
        math = int(input('What is the solution for that 2 + 2 * 2: '))
        if math == 6:
            print('Good job you won')
        else:
            print('Game over')
    else:
        print("Game over")
else:
    print('Game over')
