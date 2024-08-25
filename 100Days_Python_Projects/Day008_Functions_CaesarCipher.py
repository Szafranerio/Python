name = input('What is your name?: ')


def greet(name):
    print(f'Hello World {name}')
    print('Hello Aalborg')
    print('You are the best!')


greet(name)

age = int(input('What is your age: '))


def life_in_weeks(age):

    age_to_ninty = 90 - age
    weeks = age_to_ninty * 52
    print(f'You have {weeks} weeks left')


life_in_weeks(age)


def life_in_weeks(age):

    age_to_ninty = 90 - age
    weeks = age_to_ninty * 52
    print(f'You have {weeks} weeks left')


life_in_weeks(27)


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'Are you in {location}?')


greet_with(location='Aalborg', name='Bartek')

# Cesar cipher

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]

direction = input(
    'Type encode to code the message or decode to see the message: ').lower()
text = input('Type your message: ')
shift = int(input('Type the shift number: '))


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f'Here is coded message {output_text}')


should_continiue = True

while should_continiue:
    direction = input(
        'Type encode to code the message or decode to see the message: ').lower()
    text = input('Type your message: ')
    shift = int(input('Type the shift number: '))

    ceaser(text, shift, direction)
    restart = input('Do you want to go again?: y for Yes, n for No?\n').lower()
    if restart == "n":
        should_continiue = False
        print('Goodbye')
