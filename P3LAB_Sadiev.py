# CTI-110 
# P3LAB - Determine a grade 
# Sadiev 
# 09/13/2018
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # Variables to represent the grade thresholds
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    #Get a test score from the user.
    score = int(input('Enter a test score: '))

    #Determine the grade.
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F') 


# program start
main()
