from score import Score
from ball import Ball
from turtle import Screen
from paddle import Paddle
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("ping pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        ball_speed *= 0.8

    if ball.xcor() > 380:
        ball.reset_position()
        ball_speed = 0.1
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        ball_speed = 0.1
        score.r_point()
screen.exitonclick()
