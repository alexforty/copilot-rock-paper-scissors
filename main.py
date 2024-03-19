# Write a rock, paper, scissors game that is played against the computer.
# import random module
import random
# define main function that handles all the logic
def determine_winner(user_choice, computer_choice):
    valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    if user_choice not in valid_choices or computer_choice not in valid_choices:
        raise ValueError("Invalid choice")
    if user_choice == computer_choice:
        return 'Draw!'
    elif (user_choice == 'rock' and computer_choice in ['scissors', 'lizard']) or \
         (user_choice == 'paper' and computer_choice in ['rock', 'spock']) or \
         (user_choice == 'scissors' and computer_choice in ['paper', 'lizard']) or \
         (user_choice == 'lizard' and computer_choice in ['spock', 'paper']) or \
         (user_choice == 'spock' and computer_choice in ['scissors', 'rock']):
        return 'You win!'
    else:
        return 'You lose!'

def main():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ")
    computer_choice = random.choice(choices)
    print(determine_winner(user_choice, computer_choice))