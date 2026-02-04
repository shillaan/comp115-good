"""
Lab 3: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-2 (each values 50 points, 100 points in total).

Author:  <Shillan>
Due Date: This Friday (Jan. 23) 5:00pm.
    
"""

import turtle

drawing_screen = turtle.Screen()
alex = turtle.Turtle()
alex.speed(5)
alex.shape("turtle")

# Example 1: Staircase
num_steps = 10
for _ in range(num_steps):
    alex.forward(20)
    alex.left(90)
    alex.forward(20)
    alex.right(90)
alex.hideturtle()
alex.clear()

# Example 2: Triangle 
alex.showturtle()
alex.speed(1)
side_length = 100
exterior_angle = 360 / 3
for _ in range(3):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.hideturtle()
alex.clear()

# Example 3: Square 
alex.showturtle()
alex.up()
alex.goto(0, 0)
alex.down()
side_length = 200
exterior_angle = 360 / 4
for _ in range(4):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.hideturtle()
alex.clear()

# Exercise 1: Hexagon
alex.showturtle()
num_sides = 6
side_length = 100
exterior_angle = 360 / num_sides
for _ in range(num_sides):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.hideturtle()
alex.clear()

# Exercise 2: Rainbow 
num_circles = 7
rainbow_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
radius = 30
radius_increase = 10
alex.clear()
alex.speed(5)
alex.pensize(5)
alex.up()
for rainbow_color in rainbow_colors:
    alex.color(rainbow_color)
    alex.goto(0, -radius)
    alex.down()
    alex.circle(radius)
    alex.up()

    radius = radius + radius_increase


alex.shape("blank")



# Redoing Rainbow again

num_circles = 7
rainbow_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
radius = 30
radius_increase = 10
alex.clear()
alex.speed(5)
alex.pensize(radius_increase)
alex.up()
for rainbow_color in rainbow_colors:
    alex.color(rainbow_color)
    alex.setheading(90)
    alex.goto(-radius, 0)
    alex.down()
    alex.circle(radius, 180)
    alex.up()

    radius = radius + radius_increase


alex.shape("blank")






"""
Well done! Now you've finished your lab3 successfully. Please upload it 
to your GitHub repository and submit your lab3 GitHub link on e-learn, 
as you did for lab1 and lab2. That's all.

Resource (optional): For exercise 1, feel free to review the concept of exterior angles of regular polygons from here:
https://www.teachoo.com/8592/2789/Exterior-Angles-of-Regular-Polygons/category/Sum-of-Exterior-Angles-of-Polygons/
"""