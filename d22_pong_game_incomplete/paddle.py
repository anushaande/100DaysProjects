from turtle import Turtle
import random

class Paddle:
    def __init__(self, paddle_xcor, paddle_ycor) :
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle_xcor = paddle_xcor
        self.paddle_ycor = paddle_ycor
        self.paddle.speed("fastest")
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto( self.paddle_xcor, self.paddle_ycor)
    
    def up(self):
        # self.paddle.setheading(90)
        ycor = self.paddle.ycor()
        xcor = self.paddle.xcor
        if ycor < 275:
            self.paddle.goto(xcor, (ycor+10))

    def down(self):
        ycor = self.paddle.ycor()
        xcor = self.paddle.xcor
        if ycor > -275:
            self.paddle.goto(xcor, (ycor-10))
    

    

           