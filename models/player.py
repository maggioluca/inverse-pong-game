import turtle as t

class Player:
    def __init__(self,x,y):
        player = t.Turtle()
        self.player = player
        self.score = 0

        width = 5
        height = 0.3
        speed = 1

        player.shape("square")
        player.shapesize(width,height)

        player.color("black")

        player.penup()
        player.speed(speed)
        player.goto(x,y)

    def score():
        return self.score

    def set_score():
        self.score += 1
