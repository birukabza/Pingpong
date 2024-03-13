from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, Position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.penup()
        self.goto(Position)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)


