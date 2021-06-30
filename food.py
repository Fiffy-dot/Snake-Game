from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("DeepPink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_location = random.randint(-280, 280)
        y_location = random.randint(-280, 280)
        self.goto(x_location, y_location)
