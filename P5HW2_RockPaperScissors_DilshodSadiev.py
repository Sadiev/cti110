# This program lets the user play the game of Rock, Paper, Scissors against the computer
# 10/05/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Dilshod Sadiev
#

import random

# Constants for the choices
ROCK = 1
PAPER = 2
SCISSORS = 3

# the main function 
def main():
	# The choice variables for the user and computer
	comp_choice=0
	user_choice=0
	# if both players make the same choice,
	# the game must be played again to determine the winner
	while comp_choice==user_choice:
		user_choice=0
		# generate random choice for the computer
		comp_choice=random.randint(ROCK, SCISSORS)
		# repeat prompt user enter the choice until user input one of correct word ("rock", "paper" or "scissors")
		while user_choice==0:
			user_choice=get_user_choice()
		# display computer's choice
		display_comp_choice(comp_choice)
		# display winner
		display_win(comp_choice, user_choice)

# this function prompt user enter the choice and return it
def get_user_choice():
	user_choice=input('Enter your choice of "rock", "paper" or "scissors": ')
	if user_choice=='rock':		
		return ROCK
	elif user_choice=='paper':
		return PAPER
	elif user_choice=='scissors':
		return SCISSORS
	else:
		return 0

# this function displays computer choice	
def display_comp_choice(comp_choice):
	if comp_choice==ROCK:
		print("The computer's choice is Rock.")
	elif comp_choice==PAPER:
		print("The computer's choice is Paper.")
	else:
		print("The computer's choice is Scissors.")

# this function displays the winner			
def display_win(comp_choice, user_choice):
	if comp_choice==ROCK and user_choice==SCISSORS:
		print('Computer is winner! The rock smashes the scissors.')
	elif user_choice==ROCK and comp_choice==SCISSORS:
		print('You are winner! The rock smashes the scissors.')
	elif comp_choice==SCISSORS and user_choice==PAPER:
		print('Computer is winner! Scissors cuts paper.')
	elif user_choice==SCISSORS and comp_choice==PAPER:	
		print('You are winner! Scissors cuts paper.')
	elif comp_choice==PAPER and user_choice==ROCK:
		print('Computer is Winner! Paper wraps rock.')
	elif user_choice==PAPER and comp_choice==ROCK:
		print('You are Winner! Paper wraps rock.')
	else:
		print('Both players make the same choice, the game must be played again to determine the winner.')

# call the main function		
main()