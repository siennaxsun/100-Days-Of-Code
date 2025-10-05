from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
import time

# set up the screen
screen = Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer()

# create a ball line in the middle
ball_lines = Ball()
ball_lines.ball_lines()

# create 2 paddles on the left/right screen
LEFT_Paddle_POS_X = -380
RIGHT_Paddle_POS_X = 370
left_paddle = Paddle(LEFT_Paddle_POS_X)
right_paddle = Paddle(RIGHT_Paddle_POS_X)

# create score board on the left/right screen
LEFT_SCORE_POS_X = -50
RIGHT_SCORE_POS_X = 80
left_score = ScoreBoard(LEFT_SCORE_POS_X)
right_score = ScoreBoard(RIGHT_SCORE_POS_X)

# right paddle in response to keyboards
screen.listen()
screen.onkey(key = "Up", fun=right_paddle.move_up)
screen.onkey(key = "Down", fun=right_paddle.move_down)



EDGE_ON_RIGHT = SCREEN_WIDTH/2-20
EDGE_ON_LEFT = -(SCREEN_WIDTH/2-20)
EDGE_ON_TOP = SCREEN_HEIGHT/2 -20
EDGE_ON_BOTTOM = -(SCREEN_HEIGHT/2 -20)


game_begin = True
game_is_on = True

if game_begin:
    # game_is_on = True
    # create a new ball that is ready to serve
    # ball = Ball()
    # new_ball = ball.serve_a_ball()


    while game_is_on:
        screen.update()
        time.sleep(0.01)

        # make the computer-controlled paddle move
        left_paddle.moving()

        # make the new_ball flying
        ball = Ball()
        new_ball = ball.serve_a_ball()
        ball.fly_to_opponent(new_ball)
        print(new_ball.xcor(), new_ball.ycor())


        # check if ball collide with paddle, if it does, then bounce itself backwards
        for segment in left_paddle.paddle:
            if new_ball.distance(segment) < 10:
                print (True)
                ball.bouncing_from_left_paddle(new_ball)
        for segment in right_paddle.paddle:
            if new_ball.distance(segment) < 10:
                print(True)
                ball.bouncing_from_right_paddle(new_ball)

        # check if ball collide with top/bottom wall, if it does, then bounce itself backwards
        if new_ball.ycor() >= EDGE_ON_TOP:
            print(True)
            ball.bouncing_from_top_wall(new_ball)
        elif new_ball.ycor() <= EDGE_ON_BOTTOM:
            print(True)
            ball.bouncing_from_bottom_wall(new_ball)


        if new_ball.xcor() > EDGE_ON_RIGHT:
            print("ball_missing= True")
            ball_missing = True
            # opponent score up
            left_score.score_update(LEFT_SCORE_POS_X)
            # serve a new ball towards player
            # ball = Ball()
            # new_ball.serve_a_ball()
            # ball.fly_to_player(new_ball)
        elif new_ball.xcor() < EDGE_ON_LEFT:
            print("ball_missing= True")
            ball_missing = True
            # player score up
            right_score.score_update(RIGHT_SCORE_POS_X)
            # serve a new ball towards opponent
            # ball = Ball()
            # new_ball.serve_a_ball()
            # ball.fly_to_opponent(new_ball)
        else:
            ball_missing = False



"""
        # check score: who wins first and game over
        if left_score.final_score >= 10 or right_score.final_score >= 10:
            # print who wins
            # game over
            game_is_on = False
            # ask if replay
        else:
            # check if missing a ball: update score and serve a new ball as long as the game is not over yet
            if new_ball.xcor() > EDGE_ON_RIGHT:
                ball_missing = True
                # opponent score up
                left_score.score_update(LEFT_SCORE_POS_X)
                # serve a new ball towards player
                ball = Ball()
                new_ball.serve_a_ball()
                ball.fly_to_player(new_ball)
            elif new_ball.xcor() < EDGE_ON_LEFT:
                ball_missing = True
                # player score up
                right_score.score_update(RIGHT_SCORE_POS_X)
                # serve a new ball towards opponent
                ball = Ball()
                new_ball.serve_a_ball()
                ball.fly_to_opponent(new_ball)
            else:
                ball_missing = False

"""




screen.exitonclick()