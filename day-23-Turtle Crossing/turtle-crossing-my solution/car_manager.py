from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# CarManager:
# 1. allow to create a 2-segment square turtle as one car
# 2. this single car has a random color
# 4. this single car starts at a random x position, with y_pos from (-30, 250)
# 5. has a move(), which the car moves at a random starting speed, which increases when leveling up

class CarManager (Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.segments = []
        self.create_a_car()
        self.head = self.segments[0]


    def add_a_segment(self):
        segment = Turtle(shape="square")
        segment.setheading(180)
        segment.penup()
        # x_pos = random.uniform(300, 600)
        # y_pos = random.uniform (-200, 200)
        # segment.goto(x_pos, y_pos)
        # self.car.append(segment)
        return segment


    def create_a_car(self):
        color = random.choice(COLORS)
        x_pos = random.uniform(300, 1000)
        y_pos = random.uniform(-200, 200)
        segment_count = 3
        for i in range(0, segment_count):
            x_pos = x_pos + 20*i
            segment = self.add_a_segment()
            segment.color(color)
            segment.goto(x_pos, y_pos)
            self.segments.append(segment)


    def move(self, current_level, prev_level):
        speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (current_level - prev_level)
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(speed)

