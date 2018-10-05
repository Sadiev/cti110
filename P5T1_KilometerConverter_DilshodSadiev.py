# This program converts kilometers to miles
# 09/27/2018
# CTI-110 P5T1_KilometerConverter 
# Dilshod Sadiev
#

CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it
def main():
	# Get the distance in kilometrs
	kilometers=float(input('Enter a distance in kilometrs: '))
	
	# Display the distance converted to miles
	show_miles(kilometers)

# The show_miles function converts the parametr km from
# kilometers to miles and displays the result	
def show_miles (km):
	# Calculate miles
	miles = km * CONVERSION_FACTOR
	
	# Display the miles
	print (km, 'kilometers equals', miles, 'miles.')
	
# Call the main function
main()