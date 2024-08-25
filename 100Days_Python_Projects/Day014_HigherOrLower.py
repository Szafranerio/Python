import random
from game_data import data

print('Welcome to the higher or lower game!')


def random_choice():
    return random.choice(data)


def data_format(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description} from {country}"


def check_answer(decision, a_follower, b_follower):
    if a_follower > b_follower:
        return decision == 'A'
    else:
        return decision == 'B'


def game():
    score = 0
    game_continue = True
    account_a = random_choice()
    account_b = random_choice()

    while game_continue:
        account_a = account_b
        account_b = random_choice()

        # Ensure account_a and account_b are not the same
        while account_a == account_b:
            account_b = random_choice()

        print(f'Compare A: {data_format(account_a)}')
        print("vs")
        print(f'Compare B: {data_format(account_b)}')

        decision = input(
            "Type 'A' to vote for the first or 'B' to vote for the second: ").upper()
        a_follower = account_a['follower_count']
        b_follower = account_b['follower_count']
        is_correct = check_answer(decision, a_follower, b_follower)

        if is_correct:
            score += 1
            print('\n' * 20)  # Clears the screen
            print(f'You were right! Your current score is {score}.')
        else:
            game_continue = False
            print(f'You are wrong. Game over! Your final score was {score}.')


game()
