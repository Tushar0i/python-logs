# importing a library
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice,"computer":computer_choice}

    return choices

def check_win(player,computer):

    print(f"You choose {player}, Computer choose {computer}")

    if player == computer:
        return "It is a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock! You loose! 🙃"
        else:
            return "Rock smashes scissors! You won! 🥳"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You loose! 🙃"
        else:
            return "Paper covers rock! You won! 🥳"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You loose! 🙃"
        else:
            return "Scissors cuts paper! You won! 🥳"
    else:
        return "Enter a valid value"   
choices = get_choices()
result = check_win(choices["player"],choices["computer"])

print(result)


    