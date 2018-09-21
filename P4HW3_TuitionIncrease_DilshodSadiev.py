# This program displays tuition amount witch increase by 3 percent each year for the next 5 years
# 09/21/2018
# CTI-110 P4HW3 - Tuition Increase
# Dilshod Sadiev
#

# initialize accumulator variables
tuition=8000.00
year=2018

print('The tuition for a full-time student is $8,000 per semester.\nThe tuition will increase by 3 percent each year for next 5 years.\n')

# display the tuition amount for next 5 years
for i in range(5):
	tuition+=(tuition*3)/100	# increase tuition amout by 3 percent
	year+=1						# jump to next year
	print ('The tuition for a full-time student will be $',format(tuition,',.2f'),'per semester in', year)
	
	
input("Press any key to exit")