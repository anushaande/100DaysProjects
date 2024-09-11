from turtle import Turtle, Screen
from snake import Snake


snake = Snake()
my_screen = snake.create_canvas()
my_snake = snake.create_snake()
game_on = True
count = 0
while game_on:
    snake.move_forward()
    count +=1
    if count == 5:
        game_on = False





my_screen.exitonclick()