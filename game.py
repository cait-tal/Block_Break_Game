# Handles creation of bricks, movement of ball, and creation/movement of paddle

from turtle import Turtle

STRETCH_WIDTH = 1
STRETCH_HEIGHT = 7

#------------------------------Paddleboard--------------------------------------------#
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
        self.setpos(position)

    def move_left(self):
        self.backward(20)

    def move_right(self):
        self.forward(20)

#-------------------------------------Ball-----------------------------------------#
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.reset_speed = 0.1
        self.is_moving = False

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.8

    def bounce_x(self):
        self.x_move *= -1

    def reset(self, position):
        self.setpos(position)
        self.ball_speed = self.reset_speed
        self.is_moving = False

    def start(self):
        if self.ycor() == -280:
            self.is_moving = True
        else:
            pass

#--------------------------Blocks----------------------------------------#
BLOCK_WIDTH = 2
BLOCK_HEIGHT = 4

class Block(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color(color)
        self.shapesize(BLOCK_WIDTH, BLOCK_HEIGHT)
        self.setpos(position)

class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("white")
        self.font = ("Arail", 30, "normal")
        self.setpos(0, -100)

    def Start_Game(self):
        self.write("Press Space to Play", font=self.font, align="center")

    def Play_Again(self):
        self.write("Game Over\nPress Space to Play Again", font=self.font, align="center")

    def Next_Level(self, level):
        self.write(f"Level {level}\nPress Space to Begin", font=self.font, align="center")