from turtle import Turtle
import math
import random


# create the xy values for the paddle's segment's position on left/right screen
LEFT_POS_X = -380
RIGHT_POS_X = 380
TOP_WALL_EDGE = 280
BOTTOM_WALL_EDGE = -280
POS_Y = [-40, -20, 0, 20, 40]
DISTANCES = [-50, -30, -10, 10, 30, 50]

class Paddle(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.paddle = []
        self.create_a_paddle(pos_x)
        self.head = self.paddle[0]
        self.tail = self.paddle[-1]

    def create_a_paddle(self, pos_x):
        for y in POS_Y:
            self.add_a_segment(pos_x, y)

    def add_a_segment(self, pos_x, pos_y):
        new_segment = Turtle(shape="square")
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos_x, pos_y)

        # because by default, the turtle faces to right, and the paddle needs to move up/down
        # so better to correct its heading when create it, otherwise, when it move up/down,
        # you will notice the turtle are moving seperate from the following turtle
        current_heading = new_segment.heading()
        if current_heading!= 90:
            new_segment.setheading(90)
        new_segment.showturtle()
        self.paddle.append(new_segment)

    # computer controlled moving paddle
    def moving(self):
        # set a random speed
        speeds = ["fastest", "fast", "normal", "slow", "slowest"]
        speed = random.choice(speeds)
        # set a random moving distance
        distances = [-50, -30, -10, 10, 30, 50]
        moving_dist = random.choice(distances)

        if moving_dist > 0: # upwards
            for seg_num in range(0, len(self.paddle) - 1):
                new_x = self.paddle[seg_num + 1].xcor()
                new_y = self.paddle[seg_num + 1].ycor()
                self.paddle[seg_num].goto(new_x, new_y)
            self.tail.speed(speed)
            self.tail.forward(20)
            self.detect_wall()


        if moving_dist < 0: # backwards
            for seg_num in range(len(self.paddle) - 1, 0, -1):
                new_x = self.paddle[seg_num - 1].xcor()
                new_y = self.paddle[seg_num - 1].ycor()
                self.paddle[seg_num].goto(new_x, new_y)
            self.head.speed(speed)
            self.head.backward(20)
            self.detect_wall()



    # keyboard controlled moving paddle
    def move_up(self):
        for seg_num in range(0, len(self.paddle)-1):
            new_x = self.paddle[seg_num+1].xcor()
            new_y = self.paddle[seg_num+1].ycor()
            self.paddle[seg_num].goto(new_x, new_y)
        self.tail.forward(20)
        # detect if it is colliding with the top wall
        tail_y = self.tail.ycor()
        if tail_y > TOP_WALL_EDGE:
            self.move_down()

    def move_down(self):
        # for segment in self.paddle:
        #     segment.backward(10)
        for seg_num in range(len(self.paddle)-1, 0, -1):
            new_x = self.paddle[seg_num-1].xcor()
            new_y = self.paddle[seg_num-1].ycor()
            self.paddle[seg_num].goto(new_x, new_y)
        self.head.backward(20)
        # detect if it is colliding with the bottom wall
        head_y = self.head.ycor()
        if head_y < BOTTOM_WALL_EDGE:
            self.move_up()


    # detect wall collsion
    def detect_wall(self):
        # check head and tail's y coordinates
        head_y = self.head.ycor() #-30
        tail_y = self.tail.ycor() # 30
        # if tail_y > TOP_WALL_EDGE or head_y < BOTTOM_WALL_EDGE:
        #     return True
        # else:
        #     return False
        if tail_y > TOP_WALL_EDGE:
            self.move_down()
        if head_y < BOTTOM_WALL_EDGE:
            self.move_up()


    def stop_moving_further(self):
        pass