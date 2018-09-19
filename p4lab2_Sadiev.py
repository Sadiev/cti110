# This program displays my first and last initials
# 09/18/2018
# CTI-110 P4LAB2 - Initials
# Dilshod Sadiev
#

import turtle				# Allows us to use turtles

turtle.shape("blank")		# Make the arrow invisible
turtle.pensize(4)           # increase pensize
turtle.pencolor("blue")     # set pencolor

# Draw a letter 'D'
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.right(60)
turtle.forward(10)
turtle.right(30)
turtle.forward(33)
turtle.right(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(25)
turtle.right(180)

 # This moves turtle, but no line is drawn	
turtle.penup()
turtle.forward(50)
turtle.pendown()

# Draw a letter 'S'
turtle.forward(25)
turtle.left(60)
turtle.forward(5)
turtle.left(30)
turtle.forward(18)
turtle.left(60)
turtle.forward(5)
turtle.left(30)
turtle.forward(20)
turtle.right(60)
turtle.forward(5)
turtle.right(30)
turtle.forward(17)
turtle.right(30)
turtle.forward(5)
turtle.right(60)
turtle.forward(25)
turtle.right(90)
turtle.forward(5)



 # Wait for user to close window	
turtle.exitonclick()