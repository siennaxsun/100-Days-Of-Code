from turtle import Turtle, Screen

screen = Screen()

tim = Turtle (shape = "square")

tim.setheading(90)
# tim.right(320)

def move_up():
    tim.forward(20)
    print (tim.ycor())
    return tim.ycor()

def move_down():
    tim.backward(20)
    # print(tim.position())
    return tim.ycor()

screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)

game_is_on = True
while game_is_on:
    position = move_up()
    print ("position = " + str(position))

# def tim_position():
#     # keyboard listening: turtle moves in response to the keyboard keys
#     screen.listen()
#     screen.onkey(key="Up", fun=move_up)
#     screen.onkey(key="Down", fun=move_down)
#     y_pos = tim.ycor()
#     print(y_pos)  # why output 0?
#     return y_pos

# game_is_on = True
# while game_is_on:
#     # print (tim_position()) # why output None? because you did not return anything in the function
#     pass

# if tim.ycor() > 50:
#     screen.clearscreen()


screen.exitonclick()