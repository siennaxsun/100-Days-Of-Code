from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

"""
# my code
snakes = []
for i in range(0, 3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    # print(tim.get_shapepoly())
    moving_dist = i * 20
    tim.forward(moving_dist)
    snakes.append(tim)

step = 10

def snake_moving_up():
    turn_direction = False
    current_heading = snakes[0].heading()
    if current_heading != 90:
        turn_direction = True
    if turn_direction:
        if current_heading == 0:
            for i in range(0, len(snakes)):
                snakes[i].setheading(90)
                x_moving_dist = 20*i
                y_moving_dist = 20*i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos - x_moving_dist, y_pos + y_moving_dist)
        elif current_heading == 180:
            for i in range(0, len(snakes)):
                snakes[i].setheading(90)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos + y_moving_dist)
        elif current_heading == 270:
            for i in range(0, len(snakes)):
                snakes[i].setheading(90)
                y_moving_dist = 20 * (i-1)*2
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos, y_pos + y_moving_dist)
    for snake in snakes:
        snake.forward(step)


def snake_moving_down():
    turn_direction = False
    current_heading = snakes[0].heading()
    if current_heading != 270:
        turn_direction = True
    if turn_direction:
        if current_heading == 0:
            for i in range(0, len(snakes)):
                snakes[i].setheading(270)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos - x_moving_dist, y_pos - y_moving_dist)
        if current_heading == 180:
            for i in range(0, len(snakes)):
                snakes[i].setheading(270)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos - y_moving_dist)
        if current_heading == 90:
            for i in range(0, len(snakes)):
                snakes[i].setheading(270)
                y_moving_dist = 20 * (i-1)*2
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos, y_pos - y_moving_dist)
    for snake in snakes:
        snake.forward(step)


def snake_moving_right():
    turn_direction = False
    current_heading = snakes[0].heading()
    if current_heading != 0:
        turn_direction = True
    if turn_direction:
        if current_heading == 90:
            for i in range(0, len(snakes)):
                snakes[i].setheading(0)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos - y_moving_dist)
        if current_heading == 270:
            for i in range(0, len(snakes)):
                snakes[i].setheading(0)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos + y_moving_dist)
        if current_heading == 180:
            for i in range(0, len(snakes)):
                snakes[i].setheading(0)
                x_moving_dist = 20 * (1-i) * 2
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos)
    for snake in snakes:
        snake.forward(step)

def snake_moving_left():
    turn_direction = False
    current_heading = snakes[0].heading()
    if current_heading != 180:
        turn_direction = True
    if turn_direction:
        if current_heading == 90:
            for i in range(0, len(snakes)):
                snakes[i].setheading(180)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos - x_moving_dist, y_pos - y_moving_dist)
        if current_heading == 270:
            for i in range(0, len(snakes)):
                snakes[i].setheading(180)
                x_moving_dist = 20 * i
                y_moving_dist = 20 * i
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos - x_moving_dist, y_pos + y_moving_dist)
        if current_heading == 0:
            for i in range(0, len(snakes)):
                snakes[i].setheading(180)
                x_moving_dist = 20 * (1 - i) * 2
                x_pos = snakes[i].xcor()
                y_pos = snakes[i].ycor()
                snakes[i].goto(x_pos + x_moving_dist, y_pos)
    for snake in snakes:
        snake.forward(step)


screen.listen()
screen.onkey(key="Up", fun = snake_moving_up)
screen.onkey(key="Down", fun = snake_moving_down)
screen.onkey(key="Left", fun = snake_moving_left)
screen.onkey(key="Right", fun = snake_moving_right)

"""

# teacher's version




from snake import Snake
from food import Food
from score import ScoreBoard





tim = Snake()
foodie = Food()
score = ScoreBoard()
# high_score = ScoreBoard()

BOUNDING_EDGE = 280
game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=tim.moving_up)
screen.onkey(key="Down", fun = tim.moving_down)
screen.onkey(key="Left", fun = tim.moving_left)
screen.onkey(key="Right", fun = tim.moving_right)



while game_is_on:
    screen.update()
    time.sleep(0.3)

    tim.moving()

    # detect collision with food: using a method from Turtle class called .distance()
    if tim.head.distance(foodie) < 15:
        foodie.move_to_new()
        score.clear()
        score.increase_score()
        tim.grow_tail()

    # current_score = score.score

    # detect collision with the wall
    if tim.head.xcor() > BOUNDING_EDGE or tim.head.xcor() < - BOUNDING_EDGE or tim.head.ycor() > BOUNDING_EDGE or tim.head.ycor() < - BOUNDING_EDGE:
        # game_is_on = False
        # score.game_over()
        # highest_score = high_score_update(highest_score, current_score)
        score.reset()
        tim.reset()



    # detect collision with its own tails
    for segment in tim.segments:
        if segment == tim.head:
            pass
        elif tim.head.distance(segment) < 10:
            # score.game_over()
            # highest_score = high_score_update(highest_score, current_score)
            # game_is_on = False
            score.reset()
            tim.reset()




screen.exitonclick()