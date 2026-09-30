import random

words = ["python", "computer", "programming", "developer", "science"]

chosen_word = random.choice(words)

display_word = ["_"] * len(chosen_word)

incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display_word))

while incorrect_guesses < 6 and "_" in display_word:

    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in chosen_word:
        print("Correct guess!")

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses += 1

    print("Word:", " ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

# Final result
if "_" not in display_word:
    print("\n🎉 You won!")
else:
    print("\n💀 You lost!")
    print("The word was:", chosen_word)