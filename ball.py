import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.movement_x = 10
        self.movement_y = 10
        self.starting_position()
        self.movement_speed = 0.1

    def starting_position(self):
        starting_y = random.randint(-260, 260)
        self.goto(0, starting_y)

    def move (self):
        x_pos = self.xcor() + self.movement_x
        y_pos = self.ycor() + self.movement_y
        self.goto(x_pos, y_pos)

    def bounce_in_y(self):
        """Reverses the direction of the ball in y-axis so it bounces off the wall"""
        self.movement_y *= -1

    def bounce_in_x(self):
        """Reverses the direction of the ball in x-axis so it bounces off the paddle"""
        self.movement_x *= -1
        self.movement_speed *= 0.9

    def location_reset(self):
        self.starting_position()
        self.movement_speed = 0.1
        self.bounce_in_x()

