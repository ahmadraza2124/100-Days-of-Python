import random
from data import data

def return_random_data():
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

def check_ans(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'

def game():
    score = 0
    game_should_run = True
    account_a = return_random_data()
    account_b = return_random_data()

    while account_a == account_b:
        account_b = return_random_data()

    while game_should_run:
        print(f"\nCompare A: {format_data(account_a)}")
        print("vs")
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()

        a_account_followers = account_a['follower_count']
        b_account_followers = account_b['follower_count']

        is_correct = check_ans(guess, a_account_followers, b_account_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b
            account_b = return_random_data()
            while account_a == account_b:
                account_b = return_random_data()
        else:
            game_should_run = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
