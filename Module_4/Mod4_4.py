import random
number_to_guess = random.randint(1,10)

while True:
    user_guess = input("Guess the number between 1 and 10: ")

    # To check the entered number is valid or not
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < number_to_guess:
            print("Too low.")
        elif user_guess > number_to_guess:
            print("Too high.")
        else:
            print("Correct!")
            break
    else:
        print("Invalid input. Please enter a valid number.")
