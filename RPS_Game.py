'''
How to play Rock, Paper, Scissors 

Given a choice of rock, paper or scissors
When one of these items are shown, 
Then either:

Rock beats Scissors, but loses to Paper 

Rock > Scissors 
Rock < Paper 

Scissors beats Paper, but loses to Rock 

Scissors > Paper 
Scissors < Rock 

Paper beats Rock, but loses to Scissors 

Paper > Rock 
Paper < Scissors 

'''

import random


options = ["rock", "paper", "scissors"]
outcomes = {
    ("rock", "paper"): False,
    ("rock", "scissors"): True,
    ("rock", "rock"): None,
    ("paper", "paper"): None,
    ("paper", "scissors"): False,
    ("paper", "rock"): True,
    ("scissors", "paper"): True,
    ("scissors", "scissors"): None,
    ("scissors", "rock"): False,
}


def display_options():
    for idx, choice in enumerate(options, start=1):
        print(f"({idx}) {choice.capitalize()}")


def get_human_choice():
    choice = input("Enter the number of your choice: ")
    choice = options[int(choice) - 1]
    return choice


def get_computer_choice():
    choice = random.choice(options)
    return choice


def display_choices(human_choice, computer_choice):
    print(f"You chose {human_choice}")
    print(f"The computer chose {computer_choice}")


def get_win_lose(human_choice, computer_choice):
    return outcomes.get((human_choice, computer_choice))


def display_result(human_choice, computer_choice):
    win_lose = get_win_lose(human_choice, computer_choice)

    if win_lose is None:
        print("Draw!")
        return

    if win_lose:
        print(f"Yes, {human_choice} beat {computer_choice}!")
    else:
        print(f"Sorry, {computer_choice} beat {human_choice}")


def game():
    display_options()
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    display_choices(human_choice, computer_choice)
    display_result(human_choice, computer_choice)

game()


