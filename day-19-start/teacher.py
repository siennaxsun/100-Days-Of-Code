from turtle import Turtle, Screen


screen = Screen()

#set up the width and height of the screen
screen.setup(width=500, height=400)

# prompt the dialogue box for user to bet a winner
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")

tim = Turtle(shape = "turtle")
tim.penup()
tim.goto(x = -230, y = 0)

#create 6 turtles with one color from the colors list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tim.color("red")
tim.stamp()

tim.setheading(90)
tim.forward(30)
tim.color("orange")
tim.stamd()

screen.exitonclick()