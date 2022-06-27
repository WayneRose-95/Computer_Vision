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

class RockPaperScissors:

    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.outcomes = {
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


    def display_options(self):
        for idx, choice in enumerate(self.options, start=1):
            print(f"({idx}) {choice.capitalize()}")


    def get_human_choice(self):
        choice = input("Enter the number of your choice: ")
        choice = self.options[int(choice) - 1]
        return choice


    def get_computer_choice(self):
        choice = random.choice(self.options)
        return choice


    def display_choices(self, human_choice, computer_choice):
        print(f"You chose {human_choice}")
        print(f"The computer chose {computer_choice}")


    def get_win_lose(self, human_choice, computer_choice):
        return self.outcomes.get((human_choice, computer_choice))


    def display_result(self, human_choice, computer_choice):
        win_lose = self.get_win_lose(human_choice, computer_choice)

        if win_lose is None:
            print("Draw!")
            return

        if win_lose:
            print(f"Yes, {human_choice} beat {computer_choice}!")
        else:
            print(f"Sorry, {computer_choice} beat {human_choice}")


def start_game():
    new_game = RockPaperScissors()
    new_game.display_options()
    human_choice = new_game.get_human_choice()
    computer_choice = new_game.get_computer_choice()
    new_game.display_choices(human_choice, computer_choice)
    new_game.display_result(human_choice, computer_choice)

start_game()


