from turtle import Turtle, Screen
import random

BOUNDING = 250
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-BOUNDING, BOUNDING)
        random_y = random.randint(-BOUNDING, BOUNDING)
        self.goto(random_x, random_y)
        self.move_to_new()
        # self.xcor()
        # self.ycor()


    def detect_collision(self):
        pass
        # do this in main.py

    def move_to_new(self):
        new_x = random.randint(-BOUNDING, BOUNDING)
        new_y = random.randint(-BOUNDING, BOUNDING)
        self.goto(new_x, new_y)


