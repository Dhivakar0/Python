import turtle
import random


screen = turtle.Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Make a guess!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","blue","green","yellow","orange","violet"]
y_coordinates = [-90,-50,-10,30,70,110]
is_race_on = False
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == guess:
                print(f"you win! {winning_turtle} turtle is the winner!")
            else:
                print(f"you lose! {winning_turtle} turtle is the winner!")











screen.exitonclick()