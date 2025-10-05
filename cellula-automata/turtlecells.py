from turtle import *
import random


COLORS = ["white", "black"]

class TurtleCells(Turtle):
    def __init__(self, column, row):
        super().__init__()
        # self.shape("square")
        # self.color("white")
        # self.penup()
        # self.goto(-100, 200)
        self.turtles = []
        self.cell_size(column, row)
        # self.initial_state(random_on)


    # set the size of the turtle cell
    def cell_size(self, column, row):
        prev_x = -100
        prev_y = 200
        for x in range(0, column):
            new_x = prev_x + 20*x
            for y in range(0, row):
                new_y = prev_y - 20*y
                print(new_x, new_y)
                tim = self.create_a_turtle(new_x, new_y)
                # tim = self.color("red")
                self.turtles.append(tim)
        # print(len(self.turtles))
        return self.turtles


    def create_a_turtle(self, x, y):
        new_turtle = Turtle(shape = "square")
        new_turtle.color(random.choice(COLORS))
        new_turtle.penup()
        new_turtle.goto(x, y)


    def initial_state(self, random_on):
        random_on_turtle = random.sample(self.turtles, random_on)
        for turtle in random_on_turtle:
            turtle.color("black")


    def turtle_die(self):
        for i in self.turtles:
            neighbors = []
            # find its neighbors
            pass



    def turtle_survive(self):
        pass

    def turtle_birth(self):
        pass

