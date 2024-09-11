from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
import time

snake = Snake()
my_screen = snake.create_canvas()
my_screen.tracer(0)
time.sleep(0.1)
my_screen.update()
snake.create_snake()
food = Food()
score_board = ScoreBoard()
snake.turn_snake()


game_on = True

while game_on:
    snake.move_forward()
    #detect collision with food
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.snake_grows()
    #detect collision with walls
    x = snake.snake[0].xcor()
    y = snake.snake[0].ycor()
    if x > 295 or x < -295 or y > 295 or y < -295:
        game_on = False
        score_board.game_over()
    #detect collision with tail
    for sqr in snake.snake[1:]:
        if snake.snake[0].distance(sqr) < 10:
            game_on = False
            score_board.snake_dead()

my_screen.exitonclick()