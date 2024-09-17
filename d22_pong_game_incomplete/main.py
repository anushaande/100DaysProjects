from turtle import Screen
from ball import Ball
from paddle import Paddle
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# screen.tracer(0)

ball = Ball()
ball.draw_line()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
# screen.update()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_on = True



screen.exitonclick()
#Create Paddles
#Create Score board
#create Paddle moments