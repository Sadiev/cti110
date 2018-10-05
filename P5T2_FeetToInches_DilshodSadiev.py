# This program converts feet to inches
# 09/27/2018
# CTI-110 P5T2_FeetToInches 
# Dilshod Sadiev
#

# Constant for the number of inches per foot
INCHES_PER_FOOT=12

# main function
def main():
	# Get a number of feet from the user
	feet=int(input('Enter a number of feet: '))
	
	# Convert that to inches
	print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function convers feet to inches
def feet_to_inches(feet):
	return feet * INCHES_PER_FOOT
	
# Call the main function
main()