import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(100)

for i in range(200):
    tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    tim.circle(100)
    tim.setheading(tim.heading() + 5)
    
screen = Screen()
screen.exitonclick()