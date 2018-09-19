# A bug collector collects bugs every day fo five days.
# 09/19/2018
# CTI-110 P4T2 - Bug Collector
# Dilshod Sadiev
#

# Initialize the accumulator
total = 0

# Get the bugs collected for each day.
for day in range (1, 6):
	print('Enter the bugs collected on day', day)		# Prompt the user.
	bugs=int (input()) 									# Input the number of bugs.
	total+=bugs											# Add bugs to total.
	
# Display the total bugs.
print ('You collected a total of ', total, 'bugs.\n')	

input("Press any key to exit")