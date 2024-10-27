from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)
# print("number is " + str(number))
# guess = 0
not_ended = True
easy_attempts = 10
hard_attempts = 5
if difficulty == "easy":
    attempts = easy_attempts
    print(f"You have {attempts} attempts remaining to guess the number. ")
else:
    attempts = hard_attempts
    print(f"You have {attempts} attempts remaining to guess the number. ")


def game():
    global attempts
    global not_ended
    while not_ended and attempts > 0:
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number:
            not_ended = False
            print("You Win!")
        elif guessed_number > number:
            print("Too High.\nGuess again. ")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number. ")
        else:
            print("Too Low.\nGuess again. ")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number. ")


game()
