from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-int(self.screen.window_width() / 2 - 20),
                                       int(self.screen.window_width() / 2 - 20))
        self.random_y = random.randint(-int(self.screen.window_height() / 2 - 20),
                                       int(self.screen.window_height() / 2 - 20))
        self.goto(self.random_x, self.random_y)


