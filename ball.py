from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y = 10
        self.x = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x *= -1
        self.move_speed = 0.1