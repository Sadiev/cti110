# CTI-110 
# P3HW2 - Shipping Charges 
# Sadiev 
# 09/13/2018
#
print('The program displays the shipping charges via The Fast Freight Shipping Company\n')

#Prompt the user to enter the weight of a package.
weight=float(input('Please enter the weight of a package: '))

#Calculate and display the shipping charge 
if weight<=2:
    print('The shipping charge is $',format(weight*1.50,',.2f'), sep='')
elif weight>2 and weight<=6:
	print('The shipping charge is $',format(weight*3,',.2f'), sep='')
elif weight>6 and weight<=10:
	print('The shipping charge is $',format(weight*4,',.2f'), sep='')
else:
	print('The shipping charge is $',format(weight*4.75,',.2f'), sep='')
	
input("Press any key to continue")