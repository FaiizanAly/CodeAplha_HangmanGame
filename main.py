import random

def hangman_game():
    # 5 predefined words
    words = ['python', 'hangman', 'challenge', 'program', 'developer']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman Game!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        # Show word progress
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")

        if '_' not in display_word:
            print("Congratulations! You've guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        # Input checks
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Oops! Wrong guess. You have {max_incorrect - incorrect_guesses} guesses left.")

    else:
        print(f"Sorry, you lost! The word was '{word}'.")

# To play, simply call:
hangman_game()


# Created by Faizan Ali