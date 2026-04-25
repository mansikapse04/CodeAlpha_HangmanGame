import random

# Step 1: Word list
words = ["apple", "tiger", "chair", "robot", "plant"]

# Step 2: Random word choose
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    # Check win
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - wrong_guesses)
    else:
        print("✅ Correct guess!")

# Lose condition
if wrong_guesses == max_attempts:
    print("💀 Game Over! The word was:", word)