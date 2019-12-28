import turtle as t

class Ball:
    def __init__(self,x,y):
        ball = t.Turtle()
        self.ball = ball

        width = 0.5
        height = 0.5
        speed = 0.01

        ball.shape("square")
        ball.shapesize(width,height)

        ball.color("black")

        ball.penup()
        ball.speed(speed)
        ball.goto(x,y)
