from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def display_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def left_scores(self):
        self.left_score += 1
        self.clear()
        self.display_score()

    def right_scores(self):
        self.right_score += 1
        self.clear()
        self.display_score()

