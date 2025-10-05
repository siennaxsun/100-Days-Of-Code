from turtle import Turtle
import math
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FLYING_DIST = 30


# make a list of starting y positions from -280 to 280
central_y = [-280]
ball_count = math.floor(SCREEN_HEIGHT / 40)
for i in range(1, ball_count):
    new_y = central_y[i - 1] + 40
    central_y.append(new_y)
# print(central_y)



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.ball_lines = []
        # self.balls = []
        # self.ball_lines()
        # self.serve_a_ball()

    def ball_lines(self):
        ball_lines=[]
        for y in central_y:
            ball = self.add_a_ball(y)
            ball_lines.append(ball)
        return ball_lines

    def add_a_ball(self, position_y):
        new_ball = Turtle(shape = "square")
        new_ball.hideturtle()
        new_ball.color("white")
        new_ball.penup()
        new_ball.setheading(90)
        new_ball.goto(0, position_y)
        new_ball.showturtle()
        return new_ball
        # self.balls.append(new_ball)

    # 发球: if the opponent gets a score in previous round, then in this round, the ball is served towards player
    def serve_a_ball(self):
        new_bouncing_ball = Turtle(shape = "square")
        new_bouncing_ball.hideturtle()
        new_bouncing_ball.color("white")
        new_bouncing_ball.penup()
        new_bouncing_ball.goto(0, random.choice(central_y))
        # new_bouncing_ball.showturtle()
        return new_bouncing_ball

    def fly_to_player(self, new_ball):
        # # serve a new ball
        # new_ball = self.serve_a_ball()
        #set flying direction
        angle = random.randint(0, 180)
        new_ball.right(angle)
        new_ball.showturtle()
        # flying animation
        flying_y = new_ball.ycor()
        flying_x = new_ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH/(2 * FLYING_DIST))
        for i in range(0, flying_step_count):
            if angle <= 90:
                flying_x += FLYING_DIST * math.cos(90 - angle)
                flying_y += FLYING_DIST * math.sin(90 - angle)
            elif angle > 90:
                flying_x += FLYING_DIST * math.cos(angle - 90)
                flying_y -= FLYING_DIST * math.sin(angle - 90)
            new_ball.goto(flying_x, flying_y)

    def fly_to_opponent(self, new_ball):
        # # serve a new ball
        # new_ball = self.serve_a_ball()
        # set flying direction
        angle = random.randint(0, 180)
        new_ball.left(angle)
        new_ball.showturtle()
        # flying animation
        flying_y = new_ball.ycor()
        flying_x = new_ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH / (2 * FLYING_DIST))
        for i in range(0, flying_step_count):
            if angle <= 90:
                flying_x -= FLYING_DIST * math.cos(90-angle)
                flying_y += FLYING_DIST * math.sin(90-angle)
            elif angle > 90:
                flying_x -= FLYING_DIST * math.cos(angle - 90)
                flying_y -= FLYING_DIST * math.sin(angle - 90)
            new_ball.goto(flying_x, flying_y)


    def bouncing_from_left_paddle(self, ball):
        # set flying direction
        angle = random.randint(0, 180)
        ball.right(angle)
        # flying animation
        flying_y = ball.ycor()
        flying_x = ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH / (FLYING_DIST))
        # if bouncing back from the left paddle
        for i in range(0, flying_step_count):
            if angle <= 90:
                flying_x += FLYING_DIST * math.cos(90 - angle)
                flying_y += FLYING_DIST * math.sin(90 - angle)
            elif angle > 90:
                flying_x += FLYING_DIST * math.cos(angle - 90)
                flying_y -= FLYING_DIST * math.sin(angle - 90)
            ball.goto(flying_x, flying_y)

    def bouncing_from_right_paddle(self, ball):
        # set flying direction
        angle = random.randint(0, 180)
        ball.left(angle)
        # flying animation
        flying_y = ball.ycor()
        flying_x = ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH / (FLYING_DIST))
        # if bouncing back from the right paddle
        for i in range(0, flying_step_count):
            if angle <= 90:
                flying_x -= FLYING_DIST * math.cos(90 - angle)
                flying_y += FLYING_DIST * math.sin(90 - angle)
            elif angle > 90:
                flying_x -= FLYING_DIST * math.cos(angle - 90)
                flying_y -= FLYING_DIST * math.sin(angle - 90)
            ball.goto(flying_x, flying_y)

    def bouncing_from_bottom_wall(self, ball):
        angle = random.randint(0, 90)
        flying_y = ball.ycor()
        flying_x = ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH / (FLYING_DIST))
        if flying_x < 0:
            # set flying direction
            ball.left(angle)
            for i in range(0, flying_step_count):
                flying_x += FLYING_DIST * math.cos(90 - angle)
                flying_y += FLYING_DIST * math.sin(90 - angle)
            ball.goto(flying_x, flying_y)
        elif flying_x > 0:
            ball.right(angle)
            for i in range(0, flying_step_count):
                flying_x -= FLYING_DIST * math.cos(90 - angle)
                flying_y += FLYING_DIST * math.sin(90 - angle)
            ball.goto(flying_x, flying_y)

    def bouncing_from_top_wall(self, ball):
        angle = random.randint(90, 180)
        flying_y = ball.ycor()
        flying_x = ball.xcor()
        flying_step_count = math.ceil(SCREEN_WIDTH / (FLYING_DIST))
        if flying_x < 0:
            # set flying direction
            ball.left(angle)
            for i in range(0, flying_step_count):
                flying_x += FLYING_DIST * math.cos(90 - angle)
                flying_y -= FLYING_DIST * math.sin(90 - angle)
            ball.goto(flying_x, flying_y)
        elif flying_x > 0:
            ball.right(angle)
            for i in range(0, flying_step_count):
                flying_x -= FLYING_DIST * math.cos(90 - angle)
                flying_y -= FLYING_DIST * math.sin(90 - angle)
            ball.goto(flying_x, flying_y)
