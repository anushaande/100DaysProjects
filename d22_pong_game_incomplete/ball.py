from turtle import Turtle
import random

class Ball:
    def __init__(self) :
        self.pong_ball = Turtle()
        self.centreline = Turtle()

    def create_ball(self):
        self.pong_ball.color("white")
        self.pong_ball.shape("circle")
        self.pong_ball.penup()
        self.pong_ball.shapesize(stretch_wid=1, stretch_len=1)
           
    def draw_line(self):
        self.centreline.hideturtle()
        self.centreline.speed("fastest")
        self.centreline.penup()
        self.centreline.pencolor("white")
        self.centreline.goto(0,-375)
        self.centreline.setheading(90)
        self.centreline.width(5)
        for i in range(50):
            self.centreline.pendown()
            self.centreline.forward(10)
            self.centreline.penup()
            self.centreline.forward(15)
        
    def serve_ball(self):
        random_ycor = random.randint(-350, 350)
        self.pong_ball.goto(0.00, random_ycor)
    
    def bounce_ball(self):
        xcor = self.pong_ball.xcor()
        ycor = self.pong_ball.ycor()
        self.pong_ball.goto(xcor+10, ycor+10)

