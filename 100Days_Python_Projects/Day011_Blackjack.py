import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.add(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Loss, oponent has a blackjack"
    elif u_score == 0:
        return "Win  with a blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Opponent went over, you win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lost"


user_cards = []
computer_cards = []
user_score = -1
computer_score = -1
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Your cards: {user_cards}, current core: {user_score}')
    print(f"Computer's first cards {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input('Type y for yes, type n for no')
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f'Your final hand was {user_cards}, with the score of {user_score}')

print(
    f'The computers final hand was {computer_cards}, with the score of {computer_score}')
compare(user_score, computer_score)