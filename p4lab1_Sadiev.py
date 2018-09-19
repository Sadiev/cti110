# This program draws a square and a triangle (Using turtle graphics)
# 09/18/2018
# CTI-110 P4LAB1 - Shapes
# Dilshod Sadiev
#

import turtle				# Allows us to use turtles

turtle.shape("blank")		# Make the arrow invisible

# Draw a square using 'for' loop
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

# This moves turtle, but no line is drawn	
turtle.penup()
turtle.forward(100)
turtle.pendown()

# Draw a triangle using 'for' loop
for i in range(3):
    turtle.forward(60)
    turtle.left(120)

 # Wait for user to close window	
turtle.exitonclick()