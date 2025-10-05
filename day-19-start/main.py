
# My initial code

from turtle import Turtle, Screen
import random

screen = Screen()

#set up the width and height of the screen
screen.setup(width=500, height=400)

colors = ["red", "purple", "green", "yellow", "orange", "blue"]
names = ["timmy", "tommy", "jenny", "sammy", "mike", "james"]
speed_steps = [10, 30, 15, 50, 20, 25]

y_pos = []
step = 30
y_prev = 0 - 5 - step * 2
y_pos.append(y_prev)
for i in range(1, 6):
    y_up = y_prev + step
    y_pos.append(y_up)
    y_prev = y_up
print(y_pos)

turtles = {}
turtles["name"] = names
turtles["color"] = colors
turtles["speed"] = speed_steps
turtles["y_pos"] = y_pos
print(turtles)

# print(turtles["name"][0])

class RacingTurtles:
    def __init__(self):
        # self.name = name
        self.turtle = Turtle()
        # self.turtle.color = "red"
        self.turtle.speed = 0
        # self.turtle.ycor =  0
        # self.turtle.xcor = 0

    def starting_pos(self, starting_posY):
        self.turtle.penup()
        self.turtle.goto(-(screen.canvwidth / 2) - step, starting_posY)
        self.turtle.pendown()

    def turtle_appearance(self, color):
        self.turtle.shape("turtle")
        self.turtle.color(color)

    def moving_speed(self, speed):
        self.turtle.speed = speed


def racing_turtles(turtle_count):
    racing_turtles = []
    while turtle_count > 0:
        global colors
        color = random.choice(turtles["color"])
        turtles["color"].remove(color)

        global y_pos
        # x_cor = -(screen.canvwidth / 2) - step
        y_cor = random.choice(turtles["y_pos"])
        turtles["y_pos"].remove(y_cor)

        global speed_steps
        speed = random.choice(turtles["speed"])
        turtles["speed"].remove(speed)

        turtle_count -= 1

        new_racing_turtle = RacingTurtles()
        new_racing_turtle.starting_pos(y_cor)
        new_racing_turtle.turtle_appearance(color)
        new_racing_turtle.moving_speed(speed)
        racing_turtles.append(new_racing_turtle)

    return racing_turtles

def begin_racing():
    racing_team = racing_turtles(6)
    for racing_turtle in racing_team:
        moving_step= racing_turtle.turtle.speed
        print(moving_step)
        print (racing_turtle.turtle.xcor())
        while racing_turtle.turtle.xcor() < screen.canvwidth / 2:
                racing_turtle.turtle.forward(moving_step)


######
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
begin_racing()


screen.exitonclick()



"""
#----------------------------------------------------------------------------------------
# Teacher's version

from turtle import Turtle, Screen
import random

screen = Screen()

#set up the width and height of the screen
screen.setup(width=500, height=400)

# prompt the dialogue box for user to bet a winner
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")


#create 6 turtles with one color from the colors list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -230, y=y_positions[turtle_index])
    all_turtles.append(tim)


is_race_on = False

if user_bet: #check if user makes a bet, if so, switch on the is_race_on
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        print(turtle.xcor())
        if turtle.xcor() >= 230:
            is_race_on = False
            # turtle.forward(0)
            winning_color = turtle.pencolor()
            print(winning_color)
            if user_bet == winning_color:
                print(f"You win, the winning turtle is the {winning_color} turtle")
            else:
                print(f"You lose, the winning turtle is the {winning_color} turtle")



'''
# my way of creating 6 copies of turtles
tim = Turtle(shape = "turtle")
tim.penup()
tim.goto(x = -230, y = -100)

tims = []
print (colors[-1])
for color in colors:
    tim.color(color)
    tim.stamp()
    if color != colors[-1]:
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(0)
    tims.append(tim)

print(tims)
'''




screen.exitonclick()
"""