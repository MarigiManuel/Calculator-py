import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = 25
    
    attempts = 3

    while True:
        # Get user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guessing_game()
