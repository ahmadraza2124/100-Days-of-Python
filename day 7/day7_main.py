import random

words = [
    "sunset", "breeze", "python", "rocket", "ocean",
    "whistle", "galaxy", "puzzle", "jungle", "lantern",
    "shadow", "crystal", "wander", "marble", "echo",
    "sprint", "glow", "parrot", "frost", "ember"
]

chosen_word = random.choice(words)
print(f"The word has {len(chosen_word)} letters.")

display = ["_" for _ in chosen_word]
print("Word:", " ".join(display))

end_of_game = False
lives = 6
guessed_letters = set()

while not end_of_game:
    guess = input("Guess your letter! ").lower()

    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
        continue
    else:
        guessed_letters.add(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct guess!")
    else:
        lives -= 1
        print(f"❌ Wrong guess. You have {lives} lives remaining.")
        if lives == 0:
            print("💀 Game Over. You lose!")
            print(f"The word was: {chosen_word}")
            break

    print("Word:", " ".join(display))

    if "_" not in display:
        end_of_game = True
        print("🎉 Congratulations! You guessed the word:", chosen_word)
