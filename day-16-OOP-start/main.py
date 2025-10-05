# create an object from a class/blueprint that someone else has created
# this already-created blueprinted is the turtle module, so need to first import it
# use the class turtle that is created inside the turtle module
from turtle import Turtle, Screen

# create a new turtle object named "timmy"
timmy = Turtle()
print(timmy)

# change the shape of the turtle
timmy.shape("turtle")

# change the color of the turtle
timmy.color("red")

# make the turtle move foward by 100 paces
timmy.forward(100)

# one of the other class inside turtle module is Screen(), which represents the window the turtle is gonna show up
my_screen = Screen()

# access one of the properties of the Screen class
height = my_screen.canvwidth
print(height)

# access a method of the object: allow the program continuously running until we click on the screen
my_screen.exitonclick()



import the package you installed
from prettytable import PrettyTable

# construct my_table object
my_table = PrettyTable()

# # add a title row to my_table
# my_table.field_names (["Pokemon Name", "Type"])
#
# # add a row to the table
# my_table.add_row(["Pikachu", "Electric"])
# my_table.add_row(["Squirtle", "Water"])
# my_table.add_row(["Charmander", "Fire"])

# add the first column to the table
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

# add the second column
my_table.add_column("Type", ["Electric", "Water", "Fire"])

# modifying table's attributes: the alignment
my_table.align = "l"

print(my_table)
