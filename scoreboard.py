from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(x=-270, y=250)
        self._level = 1
        self.print_score()
        self.hideturtle()

    def print_score(self):
        self.write(f'Level: {self._level}', align="left", font=FONT)

    def increase_score(self):
        self._level += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)
