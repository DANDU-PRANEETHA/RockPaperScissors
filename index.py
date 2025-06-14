import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to exit the game.")

while True:
    user = input("\nYour choice: ").lower()
    if user == "quit":
        print("Thanks for playing!")
        break
    if user not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")
