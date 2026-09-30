import random

words = ["python", "computer", "programming", "developer", "science"]

chosen_word = random.choice(words)

display_word = ["_"] * len(chosen_word)

incorrect_guesses = 0

print("Welcome to Hangman!")
print(" ".join(display_word))

while incorrect_guesses < 6 and "_" in display_word:

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print("Correct guess!")

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses += 1

    print(" ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses)

if "_" not in display_word:
    print("🎉 You won!")
else:
    print("💀 You lost!")
    print("The word was:", chosen_word)