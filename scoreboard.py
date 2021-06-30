from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.penup()
        self.put_score()

    def put_score(self):
        self.write(f"Score: {self.score} ", align="center", font=("Calibri", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.put_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :( ", align="center", font=("Calibri", 16, "normal"))