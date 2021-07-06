from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as f:
            high_score = f.read()  # get score from our file
        self.score = 0
        self.high_score = int(high_score)
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.penup()
        self.put_score()

    def put_score(self):
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score} ", align="center",
                   font=("Calibri", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.put_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.put_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER :( ", align="center", font=("Calibri", 16, "normal"))
