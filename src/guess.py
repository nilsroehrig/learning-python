import math
import random

lower_bound = 0
upper_bound = 1025

guesses = 5

hit = False

secret_number = math.floor(random.uniform(lower_bound, upper_bound))

while guesses > 0:
    print(str(guesses) + " guesses left.")
    guess = input("Enter your guess: ")
    guesses -= 1

    if not guess.isnumeric():
        print("Not a number, guess wasted!")
        continue

    guess_as_number = int(guess)

    if secret_number == guess_as_number:
        hit = True
        break

    print("Secret number is greater!") if secret_number > guess_as_number else print("Secret number is less!")

print("You win! Number was " + str(secret_number)) if hit else print("You lose! Number was " + str(secret_number))
