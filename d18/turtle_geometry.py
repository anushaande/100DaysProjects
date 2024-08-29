from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ['aquamarine', 'blue1', 'BlueViolet', 'chartreuse', 'cyan', 'DarkOliveGreen1', 'yellow', 'VioletRed']

for i in range (3,11):
    timmy.pencolor(random.choice(colors))
    for j in range(i):
        timmy.forward(100)
        timmy.right(360/i)

    
screen = Screen()
screen.exitonclick()