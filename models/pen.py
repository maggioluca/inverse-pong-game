import turtle as t

class Pen:
    def __init__(self):
        self.pen = t.Turtle()

        speed = 0

        self.pen.color("black")

        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(speed)
        self.pen.goto(0,260)

        self.pen.write("Player A: 0\t\tPlayer B: 0",align="center",font=("Courier",24,"normal"))
