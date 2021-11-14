# import another_module
#
#
# #tapped into object another_module and called variable (V icon) another_variable
# print(another_module.another_variable)

# #import turtle
# #from turtle module import Turtle class
# import turtle
# from turtle import Turtle, Screen
#
#
# #tapped into turtl object and called class (blue C icon) Turtle (capitalized to indicate class).
# # Then save the class into an object called timmy
# #timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
# print(table.align)


print(table)