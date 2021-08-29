from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong by Bunny")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # If ball collides with ball, it will bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_in_y()

    # If ball is past a mark and within range of a paddle, it collided with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_in_x()

    # If the ball misses the paddle and hits the side - walls
    if ball.xcor() > 380:
        ball.location_reset()
        scoreboard.left_scores()

    if ball.xcor() < -380:
        ball.location_reset()
        scoreboard.right_scores()



screen.exitonclick()