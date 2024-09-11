from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def frwd():
    tim.fd(10)
def bkwd():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(frwd, 'w')
screen.onkey(bkwd, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()