# This program using turtle graphics and the range() function, draw a multi-sided snowflake
# 09/19/2018
# CTI-110 P4LAB3 - Snowflake
# Dilshod Sadiev
#

import turtle				# Allows us to use turtles
import random

turtle.shape("blank")		# Make the arrow invisible
turtle.pensize(3)           # increase pensize
turtle.bgcolor("black")		# set background color

colours=["cyan", "purple", "white", "blue", "red", "green"]

# draw a snowflake with rendom colours
for i in range(10):
	turtle.pencolor(random.choice(colours))
	for i in range (2):
		turtle.forward(100)
		turtle.right(60)
		turtle.forward(100)
		turtle.right(120)
	turtle.right(36)

 # Wait for user to close window
turtle.exitonclick()