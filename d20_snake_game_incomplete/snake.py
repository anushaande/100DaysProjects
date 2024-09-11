from turtle import Turtle, Screen
import time
class Snake:
    def __init__(self):
        self.screen = Screen()
        self.snake = []
        self.size = 0.5
        self.x = 0.00
        self.y = 0.00
        self.speed = self.size * 20
    
    def create_canvas(self):
         self.screen.bgcolor('black')
         self.screen.setup(width=500, height=500)
         self.screen.title("My Snake Game")
         self.screen.tracer(0)
         return  self.screen

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
        self.screen.update()
        return self.snake
    
    def move_forward(self):
        self.screen.update()
        time.sleep(0.2)     
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_xcor = self.snake[seg_num-1].xcor()
            new_ycor = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_xcor, new_ycor)
        self.snake[0].forward(self.speed)
        
    def turn_right(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_xcor = self.snake[seg_num-1].xcor()
            new_ycor = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_xcor, new_ycor)
            self.snake[seg_num].setheading(90)

            