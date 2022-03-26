# print a guessing game
guess_word = "love"
guess_input = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

if guess_count < guess_limit and not out_of_guesses:
    while guess_input != guess_word:
        guess_input = input("enter a secret word: ")
        guess_count += 1
else:
    out_of_guesses = True

if out_of_guesses:
    print("You lose")
else:
    print("you win")
