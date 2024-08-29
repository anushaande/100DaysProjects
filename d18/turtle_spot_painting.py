import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(50)
tim.penup()
tim.setposition(-250,-250)

def draw_dots():
    for j in range(10):
        tim.dot(20,(random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
        tim.forward(60)
        tim.dot(20,(random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

def go_right():
    tim.setheading(90)
    tim.forward(60)
    tim.dot(20,(random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
    tim.setheading(0)

def go_left():
    tim.setheading(90)
    tim.forward(60)
    tim.dot(20,(random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
    tim.setheading(180) 

for i in range(10):
    draw_dots()
    go_left()
    draw_dots()
    go_right()

screen = Screen()
screen.exitonclick()