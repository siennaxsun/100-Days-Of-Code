from turtle import *
from turtlecells import TurtleCells
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("grey")
screen.tracer()

# tim1 = Turtle(shape = "square")
# tim1.color("white")
#
# tim2 = Turtle(shape = "square")
# tim2.color("white")
# tim2.goto(tim1.xcor()+20, tim2.ycor())

screen.update()
time.sleep(0.01)

cell = TurtleCells(6, 6)



def tim_collective():
    pass


screen.exitonclick()