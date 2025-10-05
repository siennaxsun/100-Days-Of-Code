import random
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVING_UP = 90
MOVING_DOWN = 270
MOVING_LEFT = 180
MOVING_RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

        # note you need to put self.head after self.create_snake(), because if putting it before
        # self.create_snake(), the segments is still an empty list

    """
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    """

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow_tail(self):
        self.add_segment(self.segments[-1].position())

    def moving(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def moving_up(self):
        if self.head.heading() != MOVING_DOWN:
            self.segments[0].setheading(MOVING_UP)
            # so this means if the current heading is not moving down, it can't moving up
            # this allows the snake to move in all the other 3 directions but can't move backwards
    def moving_down(self):
        if self.head.heading() != MOVING_UP:
            self.segments[0].setheading(MOVING_DOWN)

    def moving_left(self):
        if self.head.heading() != MOVING_RIGHT:
            self.segments[0].setheading(MOVING_LEFT)

    def moving_right(self):
        if self.head.heading() != MOVING_LEFT:
            self.segments[0].setheading(MOVING_RIGHT)


    def reset(self):
        for segment in self.segments:
            segment.goto(-500, 0)
        self.segments.clear()  # this is to remove all the segments from the self.segments list, but this
        # will not remove turtle from lignering on the screen, to remove turtle from screen, need to
        # send turtle to a location outside the screen
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        # so basically I'm resetting and initiliazing everything in the constructor


    """
    def grow_tail(self):
        # first to get the heading to know what direction the snake is on
        # and get the position of the last segment and add another segment after it
        current_heading = self.segments[0].heading
        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()

        # create a new segment
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()

        # append the new segment to the tail based on the current heading
        if current_heading == 0:
            new_segment.goto(last_x-20, last_y)
        if current_heading == 180:
            new_segment.goto(last_x + 20, last_y)
        if current_heading == 90:
            new_segment.goto(last_x, last_y - 20)
        if current_heading == 270:
            new_segment.goto(last_x, last_y + 20)

        self.segments.append(new_segment)
        return self.segments
        # print (len(self.segments))
"""




