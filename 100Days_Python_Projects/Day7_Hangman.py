import random
chosen_word = input('What is your word for a game: ')

lives = 6


print(f'Your word have: {len(chosen_word)} letters! Good luck!')

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
not_correct_letters = []

while not game_over:
    guess = input('Guess a letter: ').lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        not_correct_letters.append(guess)
        print(f'You have {lives} left')
        print(f'Used letters: {not_correct_letters}')
        if lives == 0:
            game_over = True
            print('Game over')

    if "_" not in display:
        game_over = True
        print('You win')
