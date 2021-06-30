# this file contains all snake related functionalities
from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]  # initial positions for the bits of the snake
DISTANCE_MOVED = 20  # distance the snake moves
# directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_bits = []
        self.create_snake()
        self.head_snake = self.snake_bits[0]

    def create_snake(self):
        for position in STARTING_COORDINATES:
            self.add_snake_bit(position)

    def add_snake_bit(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_bits.append(new_turtle)

    def extend(self):
        self.add_snake_bit(self.snake_bits[-1].position())

    def move(self):
        for bit in range(len(self.snake_bits) - 1, 0, -1):  # loop to go through the snake bits
            x_pos = self.snake_bits[bit - 1].xcor()
            y_pos = self.snake_bits[bit - 1].ycor()
            self.snake_bits[bit].goto(x_pos, y_pos)
        self.head_snake.forward(DISTANCE_MOVED)

    def up(self):
        if self.head_snake.heading() != DOWN:  # ensure it can't go backwards on itself
            self.head_snake.setheading(UP)

    def down(self):
        if self.head_snake.heading() != UP:  # ensure it can't go backwards on itself
            self.head_snake.setheading(DOWN)

    def left(self):
        if self.head_snake.heading() != RIGHT:  # ensure it can't go backwards on itself
            self.head_snake.setheading(LEFT)

    def right(self):
        if self.head_snake.heading() != LEFT:  # ensure it can't go backwards on itself
            self.head_snake.setheading(RIGHT)
