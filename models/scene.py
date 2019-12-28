import turtle as t

class Scene:
    def __init__(self):
        self.width = 800
        self.height = 600

        window = t.Screen()
        self.window = window

        window.title("Maggio's Pong")
        window.bgcolor("white")

        window.setup(self.width,self.height)

        window.tracer(0)
