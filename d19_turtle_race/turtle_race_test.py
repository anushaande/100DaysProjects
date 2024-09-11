from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor('black')



flag1 = Turtle()
flag1.color('white')
flag1.penup()
flag1.setpos(450, 300)

flag2 = Turtle()
flag2.color('white')
flag2.penup()
flag2.setpos(450, 300)
flag2.pendown()
flag2.goto(450,-300)

colors = ['red', 'red']
turtle_list = []
y = 260.00
x = -450.00

for i in range(2):
    tim = Turtle()
    tim.penup()
    tim.shape('turtle')
    tim.color(colors[i])
    tim.setpos(x,y)
    turtle_list.append(tim)
    y -= 60

user_bet = screen.textinput(title="Make Your Bet", prompt="Which color turtle do you think will win?")
at_goal = False
while at_goal == False:
    for timmy in turtle_list:
        timmy.speed(random.randint(80,100))
        timmy.forward(random.randint(1,10))
    for timmy in turtle_list:
        if timmy.xcor() >= 450:
            at_goal = True
            winning_turtle = timmy
            winning_turtle_color = timmy.color()
            screen.bye()
print(winning_turtle_color[0])
if user_bet == winning_turtle_color[0]:
    print(f"Congratulations!! You wont the bet.{winning_turtle_color[0]} turtle won the race")
else:
    print(f"Sorry! You lost the bet.{winning_turtle_color[0]} turtle won the race")

# screen.exitonclick()