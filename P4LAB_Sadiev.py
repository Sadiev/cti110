# This program demonstrates a nested loop
# 09/26/2018
# CTI-110 P4LAB - Nested Loops
# Dilshod Sadiev
#

import turtle				# Allows us to use turtles          
win = turtle.Screen()		# Creates a playground for turtles
star = turtle.Turtle()		# Create a turtle, assign to star
pentagon = turtle.Turtle()	# Create a turtle, assign to pentagon

# move pentagon's start point, but no line is drawn
pentagon.penup()
pentagon.right(90)
pentagon.forward(90)
pentagon.right(90)
pentagon.forward(65)
pentagon.right(180)
pentagon.pendown()

# draw a star by adding a triangle on to each side
# this uses nested loops
for i in range(5):
    # turn the other direction, so the triangle's on the outside
	for j in range(3):
		star.forward(100)
		star.right(120)
	star.forward(100)
	star.left(72)
	# draw the pentagon
	pentagon.forward(230)
	pentagon.left(72)
	
 # Wait for user to close window	
win.mainloop()  