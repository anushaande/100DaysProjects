from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        self.size = 1
        self.x = 0.00
        self.y = 0.00
        self.steps = self.size * 20
        self.speed = 100
        self.screen = Screen()
        
    def create_snake(self):   
        for i in range(3):
            sqr = Turtle()
            sqr.penup()
            sqr.color('white')
            sqr.shape('square')
            sqr.shapesize(self.size,self.size)
            sqr.setpos(self.x,self.y)
            self.snake.append(sqr)
            self.x-=((self.size/0.5)*10)
        return self.snake
    
    def create_canvas(self):
        self.screen.bgcolor('black')
        self.screen.setup(width=600, height=600)
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        return  self.screen
    
    def move_forward(self): 
        self.screen.update()
        time.sleep(0.1)    
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_xcor = self.snake[seg_num-1].xcor()
            new_ycor = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_xcor, new_ycor)
        self.snake[0].forward(self.steps)
        self.snake[0].speed(self.speed)
        
        
    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
         if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def turn_snake(self):
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")

    def snake_grows(self):
            self.screen.update()
            time.sleep(0.1) 
            xcor_tail = self.snake[-1].xcor()
            ycor_tail = self.snake[-1].ycor()
            new_xcor = xcor_tail - ((self.size/0.5)*10)
            new_ycor = ycor_tail - ((self.size/0.5)*10)
            sqr = Turtle()
            sqr.penup()
            sqr.color('white')
            sqr.shape('square')
            sqr.shapesize(self.size,self.size)
            sqr.setpos(new_xcor,new_ycor)
            self.snake.append(sqr)
    
    def snake_eat_itself(self):
        for sqr in self.snake:
            if sqr == self.snake[0]:
                pass
            elif self.snake[0].distance(sqr) < 5:
                return True
            else:
                return False
