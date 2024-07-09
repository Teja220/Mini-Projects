import random

print("Welcome to the number guessing game!")
user_level = input("Type easy or hard method to guess the number: ")

user_number = random.randint(1, 100)  # generate a random number between 1 and 100

if user_level == "easy":
    print("You have 10 chances to guess the number")
    for i in range(10):
        user_guess = int(input("Guess the number: "))
        if user_guess == user_number:
            print("You guessed the number correctly!")
            break
        elif user_guess > user_number:
            print("Your guess is too high!")
        elif user_guess < user_number:
            print("Your guess is too low!")
    else:
        print("You have used all your chances. You lose!")

elif user_level == "hard":
    print("You have 5 chances to guess the number")
    for i in range(5):
        user_guess = int(input("Guess the number: "))
        if user_guess == user_number:
            print("You guessed the number correctly!")
            break
        elif user_guess > user_number:
            print("Your guess is too high!")
        elif user_guess < user_number:
            print("Your guess is too low!")
    else:
        print("You have used all your chances. You lose!")