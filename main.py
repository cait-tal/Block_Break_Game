# Handles creation of screen and player inputs
from turtle import Screen
from game import *
import time

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.listen()

paddle = Paddle((0, -300))
ball = Ball()
ball.reset((0, -280))
text = Text()
text.Start_Game()
block_list = []
lives = 3
level = 1
broken_blocks = []

y_pos = 300
x_pos = -400
color = "dark green"

for _ in range(36):
    new_block = Block((x_pos, y_pos), color)
    block_list.append(new_block)
    x_pos += 100
    if len(block_list) == 9:
        y_pos = 240
        x_pos = -380
        color = "dark red"
    if len(block_list) == 18:
        y_pos = 180
        x_pos = -400
        color = "dark blue"
    if len(block_list) == 27:
        y_pos = 120
        x_pos = -380
        color = "gold"

screen.onkeypress(fun=paddle.move_left, key="a")
screen.onkeypress(fun=paddle.move_left, key="Left")

screen.onkeypress(fun=paddle.move_right, key="d")
screen.onkeypress(fun=paddle.move_right, key="Right")

screen.onkey(fun=ball.start, key="space")
game_is_on = True
while game_is_on:
    try:

        ball_speed = 0.1
        time.sleep(ball.ball_speed)
        screen.update()

    #-------------------Initial setup of ball-------------------#
        if ball.is_moving:
            text.clear()
            ball.move()
        else:
            ball.reset((paddle.xcor(), -280))

    #------------------Detect Collisions with Walls-------------------#

        if ball.ycor() > 340:
            ball.bounce_y()
            ball.move()

        if ball.xcor() > 440 or ball.xcor() < -440:
            ball.bounce_x()
            ball.move()

    #-------------------Detect Collisions with Paddle----------------------#
        if ball.ycor() < -285 and (paddle.xcor()-60) < ball.xcor() and ball.distance(paddle) < 51 or ball.ycor() < -285 and ball.xcor() < (paddle.xcor()+60) and ball.distance(paddle) < 51:
            ball.bounce_y()

    #-------------------Detect a Miss--------------------------------#
        if ball.ycor() < -350:
            ball.reset((paddle.xcor(), -280))
            lives -= 1

    #-------------------Detect Collision with Box------------------------#
        for block in block_list:
            if ball.distance(block) < 40 and (block.xcor()-35) < block.xcor() < (block.xcor() + 35) or ball.distance(block) < 50 and (block.ycor()-15) < block.ycor() < (block.ycor() + 15):
                block_list.remove(block)
                broken_blocks.append(block)
                block.hideturtle()
                if (block.ycor()-15) < block.ycor() < (block.ycor() + 15):
                    ball.bounce_y()
                else:
                    ball.bounce_x()

    #----------------Game Over--------------------------------------#
        if lives == 0:
            text.Play_Again()
            if ball.is_moving:
                lives = 3
                ball.reset_speed = 0.1
                for block in broken_blocks:
                    block.showturtle()
                block_list = block_list + broken_blocks

    #--------------------Next Level-----------------------------------#
        if len(block_list) == 0:
            level += 1
            text.Next_Level(level)
            ball.reset_speed += .1
            ball.reset()
            lives = 3
            if ball.is_moving:
                block_list = [block.showturtle() for block in broken_blocks]
                broken_blocks = []




    except:
        break




screen.mainloop()
