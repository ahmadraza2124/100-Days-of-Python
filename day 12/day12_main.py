# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside the funtion {enemies}")

# increase_enemies()
# print(f"enemies outside the function {enemies}")



# import random

# numbers = list(range(1, 101))

# print('Welcome to the number guessing game!')
# print("I'm thinking of a number from 1 to 100")

# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# total_attempts = 10 if difficulty == 'easy' else 5
# guessed_number = random.choice(numbers)

# print(f'You have {total_attempts} attempts remaining to guess the number.')

# while total_attempts > 0:
#     user_guess = int(input("Guess a number: "))

#     if user_guess > guessed_number:
#         total_attempts -= 1
#         print("Too High.")
#     elif user_guess < guessed_number:
#         total_attempts -= 1
#         print("Too Low.")
#     else:
#         print(f"🎉 You got it! The answer was {guessed_number}.")
#         break

#     if total_attempts == 0:
#         print(f"❌ You've run out of guesses. The number was {guessed_number}.")
#     else:
#         print(f"You have {total_attempts} attempts remaining. Guess again.")




from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too High.')
        return turns - 1
    elif guess < answer:
        print('Too Low.')
        return turns - 1
    else:
        print(f'🎉 You got it! The answer was {answer}.')
        return turns

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def start_game():
    print('Welcome to the number guessing game!')
    print("I'm thinking of a number from 1 to 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = None

    while guess != answer:
        if turns == 0:
            print(f"❌ You've run out of guesses. The answer was {answer}.")
            return
        
        print(f"\nYou have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if guess != answer and turns > 0:
            print("Guess again.")

start_game()
