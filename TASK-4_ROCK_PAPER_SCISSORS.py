# ROCK,PAPER,SCISSORS

import os
import random

while True:

    # List of choices
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = False

    while player not in choices:
        player = input("rock,paper or scissors:").lower()

    print("Computer\'s choice:",computer)
    print("Your choice:",player)

    if player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose")
        if computer == "scissors":
            print("You won")
    elif player == "scissors":
        if computer == "rock":
            print("You lose")
        if computer == "paper":
            print("You won")
    elif player == "paper":
        if computer == "rock":
            print("You won")
        if computer == "scissors":
            print("You lose")

    play_again = input("Play again(yes/no):").lower()
    if play_again == "yes":
        os.system("cls")
    else:
        break

print("BYE!!!")
