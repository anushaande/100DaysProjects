from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pencolor("red")

for i in range(30):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.bgcolor("white")
screen.exitonclick()