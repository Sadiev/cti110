# This program display the amount that the user is over or under budget.
# 09/19/2018
# CTI-110 P4HW1 - Budget Analysis
# Dilshod Sadiev
#

# get amount of budgeted for a month
budget=float(input('Enter the amount that you have budgeted for a month:' ))

# initialize an accumulator variable
expenses=0.0

# create a variable to control the loop
keep_going='y'

# get the expenses and accumulate them
while keep_going=='y' or keep_going=='Y':
	expenses=expenses+float(input('Enter your expenses for the month: '))
	keep_going=input('Do you have more expenses for the month? (Enter y for yes)')

# display the amount that the user is over or under budget	
if budget>=expenses:
	print("Your expenses are under the budget ", format(expenses,',.2f'), sep='')
else:
	print("Your expenses are over the budget ", format(expenses,',.2f'), sep='')
	
input("Press any key to exit")
	