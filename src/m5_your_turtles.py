"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Allison Shi.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(1)


turtle_1 = rg.SimpleTurtle('turtle')
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1._turtle.goto(-300, 200)
turtle_1.pen = rg.Pen('midnight blue', 3)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# H
turtle_1.right(90)
turtle_1.forward(60)
turtle_1.left(180)
turtle_1.forward(30)
turtle_1.right(90)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.right(180)
turtle_1.forward(60)
turtle_1.left(90)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(10)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# E
turtle_1.forward(30)
turtle_1.left(90)
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(30)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.right(90)
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(30)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()
turtle_1.right(90)
turtle_1.forward(30)
turtle_1.left(180)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.left(90)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(80)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# both Ls
turtle_1.forward(30)
turtle_1.left(90)
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(70)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(10)
turtle_1.left(90)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()
turtle_1.forward(60)
turtle_1.right(90)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(40)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# O
turtle_1.right(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.right(180)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(80)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# W
turtle_1.right(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.right(180)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.right(90)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(10)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# O
turtle_1.right(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.left(90)
turtle_1.forward(30)
turtle_1.right(180)

# space
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1.forward(10)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()

# R
turtle_1.forward(30)
turtle_1.right(90)
turtle_1.forward(30)
turtle_1.right(90)
turtle_1.forward(30)
turtle_1.left(145)
turtle_1.forward(42)  # 30 * root 2
turtle_1.right(180)
turtle_1.forward(42)
turtle_1.right(45)
turtle_1.forward(30)
turtle_1.right(180)
turtle_1.forward(60)

# next line
turtle_1._update_real_turtle()
turtle_1._turtle.penup()
turtle_1._turtle.goto(-300, -200)
turtle_1._update_real_turtle()
turtle_1._turtle.pendown()



# turtle_1.speed = 50  # Fast
# size = 150
# for k in range(3):
# turtle_1.draw_circle(size)
# size = size + 10
turtle_2 = rg.SimpleTurtle('turtle')
turtle_2.pen = rg.Pen('blue', 3)
# number_of_sides = 3
# for k in range(10):
#   turtle_1.draw_circle(size)
#  size = size + 10
# turtle_2.draw_regular_polygon(number_of_sides, 40)
#number_of_sides = number_of_sides + 1
