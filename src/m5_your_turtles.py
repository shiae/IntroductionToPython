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

celeste = rg.SimpleTurtle('turtle')
celeste.speed = 5
celeste._update_real_turtle()
celeste._turtle.penup()
celeste._turtle.goto(-240, 200)
celeste.pen = rg.Pen('midnight blue', 3)
celeste._update_real_turtle()
celeste._turtle.pendown()

# H
celeste.right(90)
celeste.forward(60)
celeste.left(180)
celeste.forward(30)
celeste.right(90)
celeste.forward(30)
celeste.left(90)
celeste.forward(30)
celeste.right(180)
celeste.forward(60)
celeste.left(90)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(10)
celeste._update_real_turtle()
celeste._turtle.pendown()

# E
celeste.forward(30)
celeste.left(90)
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(30)
celeste._update_real_turtle()
celeste._turtle.pendown()
celeste.left(90)
celeste.forward(30)
celeste.right(90)
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(30)
celeste._update_real_turtle()
celeste._turtle.pendown()
celeste.right(90)
celeste.forward(30)
celeste.left(180)
celeste.forward(30)
celeste.left(90)
celeste.forward(60)
celeste.left(90)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(80)
celeste._update_real_turtle()
celeste._turtle.pendown()

# both Ls
celeste.forward(30)
celeste.left(90)
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(60)
celeste.left(90)
celeste.forward(70)
celeste._update_real_turtle()
celeste._turtle.pendown()
celeste.left(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(10)
celeste.left(90)
celeste._update_real_turtle()
celeste._turtle.pendown()
celeste.forward(60)
celeste.right(90)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(40)
celeste._update_real_turtle()
celeste._turtle.pendown()

# O
celeste.right(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste.left(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste.right(180)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(80)
celeste._update_real_turtle()
celeste._turtle.pendown()

# W
celeste.right(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste.left(90)
celeste.forward(30)
celeste.right(180)
celeste.forward(30)
celeste.left(90)
celeste.forward(30)
celeste.left(90)
celeste.forward(60)
celeste.right(90)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(10)
celeste._update_real_turtle()
celeste._turtle.pendown()

# O
celeste.right(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste.left(90)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)
celeste.right(180)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(40)
celeste._update_real_turtle()
celeste._turtle.pendown()

# R
celeste.forward(30)
celeste.right(90)
celeste.forward(30)
celeste.right(90)
celeste.forward(30)
celeste.left(135)
celeste.forward(42)  # 30 * root 2
celeste.right(180)
celeste.forward(42)
celeste.right(45)
celeste.forward(30)
celeste.right(180)
celeste.forward(60)
celeste.left(90)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(40)
celeste._update_real_turtle()
celeste._turtle.pendown()

# L
celeste.left(90)
celeste.forward(60)
celeste.right(180)
celeste.forward(60)
celeste.left(90)
celeste.forward(30)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(10)
celeste._update_real_turtle()
celeste._turtle.pendown()

# D
celeste.left(90)
celeste.forward(60)
celeste.right(90)
celeste.forward(10)
celeste.right(45)
celeste.forward(14)  # 10 * root 2
celeste.right(45)
celeste.forward(40)
celeste.right(45)
celeste.forward(14)
celeste.right(45)
celeste.forward(10)
celeste.right(180)

# space
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(40)
celeste._update_real_turtle()
celeste._turtle.pendown()

# !
celeste.left(90)
celeste.forward(2)
celeste._update_real_turtle()
celeste._turtle.penup()
celeste.forward(8)
celeste._update_real_turtle()
celeste._turtle.pendown()
celeste.forward(50)

# you go, glenn coco
glenn = rg.SimpleTurtle('turtle')
glenn.pen = rg.Pen('light green', 3)
glenn.speed = 50
glenn._update_real_turtle()
glenn._turtle.penup()
glenn._turtle.goto(0, -50)
glenn._update_real_turtle()
glenn._turtle.pendown()
number_of_sides = 3
for k in range(50):
    glenn.draw_regular_polygon(number_of_sides, 30)
    number_of_sides = number_of_sides + 1
    # glenn._update_real_turtle()
    # glenn._turtle.penup()
    glenn.right(30)
    # glenn.forward(5)
    # glenn.left(90)
    glenn._update_real_turtle()
    glenn._turtle.pendown()

for k in range(5):
    celeste._update_real_turtle()
    celeste._turtle.penup()
    celeste._turtle.goto(40, -50)
    celeste.draw_circle(60)
