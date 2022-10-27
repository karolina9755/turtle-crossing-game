from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEEDS = [15, 10, 10, 10, 5, 12]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
STARTING_POSITION_Y = -280
FINISH_LINE_Y = 280


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=3)
        r = random.randint(0, 5)
        self.color(COLORS[r])
        self.move_increment = SPEEDS[r]
        self.speed("fastest")
        self.setheading(180)
        pos_x = 330
        pos_y = random.randint(STARTING_POSITION_Y+20, FINISH_LINE_Y-20)
        self.setposition(pos_x, pos_y)
        self.move()

    def move(self):
        self.forward(self.move_increment)





