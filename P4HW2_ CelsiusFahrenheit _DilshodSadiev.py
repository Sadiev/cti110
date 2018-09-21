# This program displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents
# 09/20/2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Dilshod Sadiev
#

# display column title for the table
print('Celsius \t Fahrenheit')
print('---------------------')

# convert Celsius to Fahrenheit and print them
for celsius in range(21):
	F=(9/5)*celsius +32
	print (celsius,'\t',  format(F,',.1f'))
	
input("Press any key to exit")