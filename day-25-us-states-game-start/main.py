import turtle
screen = turtle.Screen()
screen.title("U.S. States")

# you can load in an image as the turtle's shape
image = "blank_states_img.gif"
screen.addshape(image)
# once the image is loaded into the screen, it is available for turtle to use
turtle.shape(image) # change turtle shape to this image file




""" 
no need to have this line of code, because you already have the 50_states coordinates in csv file
def get_mouse_click_coor(x, y):
    print(x, y)

clicked_state = turtle.onscreenclick(get_mouse_click_coor)
print(clicked_state)
"""





import pandas

data = pandas.read_csv("50_states.csv")
print(type(data))
# output <class 'pandas.core.frame.DataFrame'>

# step 1: get all the states in a list
all_states = data.state
print(type(all_states))
# output <class 'pandas.core.series.Series'>

all_states_list = all_states.to_list()
print(all_states_list)
# output: ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


california = data[data.state =="California"]
print(california)
#         state    x   y
# 4  California -297  13


state_name = california.state
print(state_name)
# 4    California
# Name: state, dtype: object

state_name = california.state.item()
print(state_name)
# California

california_x = california.x
print(california_x)
# 4   -297
# Name: x, dtype: int64


california_x = california.x.squeeze()
print(california_x)
# -297

california_y = california.y.item()
print(california_y)
# 13

# game_is_on = True
guessed_states = []
while len(guessed_states) < 50:
    # step 2: get user's input and check whether user's input is in the above list
    user_input = screen.textinput(f"{len(guessed_states)}/50  State Correct", "What's Another State Name?").title()

    # step 3: create a state turtle, which is in the text form
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()


    # step 4: if user's input is in the list, then get that state's x and y coordinates
    # and the correct_count goes up by 1

    if user_input in all_states_list:
        print (True)
        guessed_states.append(user_input)
        coordinate = data[data.state == user_input]
        x_pos = coordinate.x.squeeze()
        y_pos = coordinate.y.squeeze()
        print (x_pos, y_pos)
        # correct_count += 1
        state_turtle.goto(x_pos, y_pos)
        state_turtle.write(user_input, align='left', font=('Arial', 8, 'normal'))

    # if user input is "exit", then break out of the while loop
    if user_input == "Exit":
        missed_states = [state for state in all_states_list if state not in guessed_states]

        missed_state_data = pandas.DataFrame(missed_states)
        print(missed_state_data)
        missed_state_csv = missed_state_data.to_csv("missed states.csv")
        break



# an alternative way to screen.exitonclick, which is to keep the screen open even though the code has finished running
turtle.mainloop()

# screen.exitonclick()