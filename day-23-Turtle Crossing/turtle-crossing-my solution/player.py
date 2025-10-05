from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Turtle player:
# 1. allow to create a single turtle shape in black
# 2. this single turtle has a fixed starting position (0, 20)
# 3. the turtle can listen to keys to move_up() and move_down()

class Player (Turtle):
    def __init__(self):
        super().__init__()
        # self.player = Turtle(shape = "turtle")
        self.shape("turtle")
        self.penup()
        self.move_to_start()
        self.setheading(90)

    def move_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        return self.ycor()

    def move_down(self):
        self.backward(MOVE_DISTANCE)
        return self.ycor()

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        return self.ycor()

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        return self.ycor()

    def screen_listening(self):
        screen = Screen()
        screen.listen()
        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key="Down", fun=self.move_down)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)
        return self.ycor()

