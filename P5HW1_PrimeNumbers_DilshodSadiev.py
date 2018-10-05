# This program determinants that a number is prime or not
# 10/04/2018
# CTI-110 P5HW1 - Prime Numbers
# Dilshod Sadiev
#

# The main function prompts the user to enter a number and
# displays a message indicating whether the number is prime
def main():
    num =int(input('Enter a number: '))
    if is_prime(num) or num==2 or num==3:
        print('The number is prime.')
    else:
        print('The number is NOT prime.')
		
# The boolean function which takes an integer as an argument and
# resum true if the argument is a prime number, or false otherwise
def is_prime(num):
	if (num%2)==0 or (num%3)==0 or num==1:
		return False
	else:	
		return True

# Call the main function
main()


