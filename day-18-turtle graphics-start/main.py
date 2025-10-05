from turtle import Turtle, Screen


screen = Screen()
screen_width = screen.canvwidth
screen_height = screen.canvheight
print(screen_width, screen_height)

timmy = Turtle()
# timmy.shape("arrow")


"""
# task 2: draw a dash line
step = 10

timmy.color("white")
timmy.setpos(-screen_width/2, 0)
print(timmy.pos())

timmy.color("medium blue")
for i in range(15):
    timmy.pendown()
    timmy.forward(step)
    timmy.penup()
    timmy.forward(step)

print(timmy.pos())
"""

"""# task 3: draw a triangle, square, pentagon, hexagon, heptagon, octagon, etc
import random

colors = ["cornflower blue", "sky blue", "medium aquamarine", "gold", "peach puff", "dark orange", "light salmon",
          "firebrick", "magenta", "maroon", "teal"]

def draw_shape(num_sides):
    angle = (num_sides - 2) * 180 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.left(angle-180)

current_color = random.choice(colors)
for i in range(3, 10):
    num_sides = i
    draw_shape(num_sides)
    prev_color = current_color
    current_color = random.choice(colors)
    if current_color != prev_color:
        timmy.color(current_color)

"""




"""# task 4: random walk

import turtle as t
import random

colors = ["cornflower blue", "sky blue", "medium aquamarine", "gold", "peach puff", "dark orange", "light salmon",
          "firebrick", "magenta", "maroon", "teal"]

angles = [0, 90, -90]
distance = 20

timmy.speed(10)
timmy.width(5)

t.colormode(255)

def random_color():
    color_r = random.randint(0, 255)
    color_g = random.randint(0, 255)
    color_b = random.randint(0, 255)
    random_color = (color_r, color_g, color_b)
    timmy.pencolor(random_color)

def draw():
    random_color()
    turning_angle = random.choice(angles)
    timmy.setheading(turning_angle)
    timmy.forward(distance)


for i in range(200):
    draw()"""

"""
# task 5: make a spirograph

import turtle as t
import random

t.colormode(1)
num_circle = 50
angle = 360/num_circle
radius = 100

timmy.speed("fastest")
timmy.width(1)

"""def random_color():
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    color = (r, g, b)
    timmy.pencolor(color)"""


shade_change = 1/num_circle
shade = 1
for i in range(num_circle):
    shade -= shade_change*200
    timmy.pencolor(shade, shade, shade)
    timmy.right(angle)
    timmy.circle(radius)"""




screen.exitonclick()