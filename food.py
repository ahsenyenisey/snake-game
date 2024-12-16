from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "black", "purple", "blue"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.65, stretch_wid=0.65)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()
        self.color(random.choice(COLORS))

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
