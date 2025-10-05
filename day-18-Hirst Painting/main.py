########################################################
# extract colors from an image
import colorgram

colors = colorgram.extract('image.jpg', 30)
# note the image has to be at the same folder level as the main.py file

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


#------------------------------------------------------------------------
# draw the spot paintints with random colors from extracted color list

import turtle as t
from turtle import Turtle, Screen
import random

# set the colormode of the module
t.colormode((255))

#set screen size
screen = Screen()
canvas_width = screen.canvwidth * 0.6
canvas_height = screen.canvheight * 0.6
print(canvas_width, canvas_height)

# create a new turtle object
timmy = Turtle()
timmy.hideturtle()

# set timmy turtle to a new position, near the left bottom corner of the canvas
timmy.penup()
timmy.goto(-canvas_width, -canvas_height)

# set the values of the size of the dot and spacing between the dots
unit_square_side_leng = 50
num_dots_row = round(canvas_width*2/unit_square_side_leng)
num_dots_column = round(canvas_height*2/unit_square_side_leng)
dot_radius = int((unit_square_side_leng / 2)*0.6)
print(num_dots_row, num_dots_column)
print(dot_radius)


def random_colors(color_list):
    new_color = random.choice(color_list)
    timmy.pencolor(new_color)


def draw_dots_row(num_dots):
    for i in range(num_dots):
        timmy.pendown()
        random_colors(rgb_colors)
        timmy.dot(dot_radius)
        timmy.penup()
        timmy.forward(unit_square_side_leng)


def turn_around(direction):
    timmy.back(unit_square_side_leng)
    timmy.left(direction)
    timmy.forward(unit_square_side_leng)
    timmy.left(direction)


# ---------------------------------------------------
# drawing
direction = -90
for i in range(num_dots_row):
    draw_dots_row(num_dots_row)
    direction *= -1
    turn_around(direction)



screen.exitonclick()

