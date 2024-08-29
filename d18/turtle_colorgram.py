import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(50)
tim.penup()
tim.setposition(-250,-250)

def get_colors():
    rgb_colors = []
    colors = colorgram.extract('./d18/img2_nature.jpeg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors

color_list = get_colors()

def draw_dots():
    for j in range(10):
        tim.dot(20,(random.choice(color_list)))
        tim.forward(60)
        tim.dot(20,(random.choice(color_list)))

def go_right():
    tim.setheading(90)
    tim.forward(60)
    tim.dot(20,(random.choice(color_list)))
    tim.setheading(0)

def go_left():
    tim.setheading(90)
    tim.forward(60)
    tim.dot(20,(random.choice(color_list)))
    tim.setheading(180) 

for i in range(10):
    draw_dots()
    go_left()
    draw_dots()
    go_right()

screen = Screen()
screen.exitonclick()


