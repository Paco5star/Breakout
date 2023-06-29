from turtle import *
import time 
import random 

screen = Screen()
player = Turtle()
screen.register_shape("bar", ((-50, -5), (50, -5), (50, 5), (-50, 5))) 

live_display = Turtle()
live_display.penup()
live_display.hideturtle()
live_display.goto(460,370)
live_display.color("black")
live_display.write("Lives: 3", align="right", font=("Arial", 16, "normal"))

game_over_display = Turtle()
game_over_display.penup()
game_over_display.hideturtle()

brick_counter = Turtle()
brick_counter.penup()
brick_counter.hideturtle()
brick_counter.goto(-340,370)
brick_counter.color("black")
brick_counter.write("Bricks left: 88", align="right", font=("Arial", 16, "normal"))

lives = 3 

def update_brick_counter():
    global blocks
    num_block = len(blocks)
    brick_counter.clear()
    brick_counter.write(f"bricks left : {num_block}", align="right", font=("Arial", 16, "normal"))

def update_lives_display():
    live_display.clear()
    live_display.write(f"Lives: {lives}", align="right", font=("Arial", 16, "normal"))

def miss_ball():
    global lives
    lives -= 1
    if lives <= 0:
        game_over_display.goto(0,0)
        game_over_display.color("black")
        game_over_display.write("GAME OVER!🤐", font=("ariel", 32, "normal"))
        game_is_on = False
    else:   
        update_lives_display()
        reset_ball()

def reset_ball():
    tracer(0,0)
    ball.goto(0,0)
    tracer(1,10)
    time.sleep(1)


player.shape("bar")
player.shapesize(2,3)
player.setheading(90)
player.penup()
player.sety(-370)

ball = Turtle()
ball.shape("circle")
ball.x_move = 5
ball.y_move = 5
ball.penup()
def move_left():
    x = player.xcor()
    x -= 40
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 40 
    player.setx(x)

def move():
    new_y = ball.ycor() + ball.y_move
    new_x = ball.xcor() + ball.x_move
    ball.goto(new_x, new_y)
    if ball.distance(player) < 100 and ball.ycor() <-350:
        ball.y_move *=-1

    for block in blocks:
        if block.isvisible() and ball.distance(block)< 40:
            ball.y_move *=-1
            block.hideturtle()
            blocks.remove(block)
            update_brick_counter()
            del block
            break 
    

block_width = 80
block_height = 20
block_colors = ["red", "green", "blue", "yellow", "pink", "purple"]
blocks = []
tracer(0,0)
for row in range(8):
    y = 340 - row * block_height * 2
    for col in range(11):
        x = col * block_width - 390
        block = Turtle()
        block.shape("square")
        block.color(random.choice(block_colors))
        block.shapesize(stretch_wid=1, stretch_len=4)
        block.penup()
        block.pensize(2)
        block.pencolor("black")
        block.goto(x,y)
        blocks.append(block)

tracer(1,10)
game_is_on = True 
while game_is_on:
    time.sleep(0.001)
    screen.update()
    move()

    if ball.ycor() > 370:
        ball.y_move *=-1
    elif ball.xcor() > 470 or ball.xcor() < -470:
        ball.x_move *=-1
    elif ball.ycor()< -380:
        miss_ball()
    
    


    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.listen()





screen.mainloop()
