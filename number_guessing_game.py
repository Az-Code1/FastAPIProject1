import random


class NumberGuessingGame:
    def __init__(self):
        # Generate the random number when object is created
        self.secret_number = random.randint(1, 100)
        print(f"DEBUG: Secret number is {self.secret_number}")  # Remove this in production

    def verify_number(self):
        try:
            guessed_number = int(input("Guess the number between 1 and 100: "))

            if guessed_number == self.secret_number:
                print("You guessed the number right!")
                return True
            elif guessed_number < self.secret_number:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")

            return False

        except ValueError:
            print("Please enter a valid number!")
            return False

    def play(self):
        """Main game loop"""
        print("Welcome to the Number Guessing Game!")
        print("I've picked a number between 1 and 100.")

        attempts = 0
        max_attempts = 10

        while attempts < max_attempts:
            attempts += 1
            print(f"\nAttempt {attempts}/{max_attempts}")

            if self.verify_number():
                print(f" You won in {attempts} attempts!")
                break
        else:
            print(f"\n Game over! The number was {self.secret_number}")


# How to play the game
game = NumberGuessingGame()  # Create instance
game.play()  # Start the game