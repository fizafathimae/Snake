import turtle
import random
import time
#creating screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")
#creating border
turtle.speed(3)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.penup()
turtle.hideturtle()
#score
score = 0;
delay = 0.1
#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.color("green")
fruit.penup()
fruit.goto(30,30)

old_fruit = []
#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score : ", align="center")
#define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"
def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"
def snake_go_left():
    if snake.direction != "right":
        snake.direction = "lrft"
def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.sety(x + 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.sety(x + 20)
#keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "up")
screen.onkeypress(snake_go_up, "down")
screen.onkeypress(snake_go_up, "left")
screen.onkeypress(snake_go_up, "right")
#main loop
while True:
    screen.update()
    #snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290,270)
        y = random.randint(-20,240)
        fruit.goto(x,y)
        scoring.clear()
        score += 1
        scoring.write("Score : {}".format(score), align="center")
        delay -=0.001
        #creating new foods
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("yellow")
        new_fruit.penup()
        old_fruit.append(new_fruit)
        #adding ball to snake
        for index in range(len(old_fruit) -1, 0, -1):
            a = old_fruit[index -1].xcor()
            b = old_fruit[index -1].ycor()

            old_fruit[index].goto(a, b)

        if len(old_fruit) > 0:
            a = snake.xcor()
            b = snake.ycor()
            old_fruit[0].goto(a, b)
        snake_move()
        #snake and border collision
        if snake.xcor() > 288 or snake.xcor() < -388 or snake.ycor() > 248 or snake.ycor() < -248:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("pink")
            scoring.goto(0, 0)
            scoring.write("Game over\n your score is {}".format(score),align="center")
        time.sleep(delay)
turtle.Terminator()   



        

    



