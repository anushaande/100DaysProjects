import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
colors = ["cyan","aquamarine","sienna", "dark green", "orchid", "dark magenta", "orange red", "deep sky blue", "dodger blue"]
directions = [0, 90, 180, 270]
timmy = Turtle()
timmy.pensize(10)
timmy.speed(100)

for i in range(500):
    timmy.right(90)
    # timmy.pencolor(random.choice(colors))
    timmy.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    

screen = Screen()
screen.exitonclick