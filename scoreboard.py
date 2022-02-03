from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    
    def update(self):
        self.clear()
        self.write(f"Score :{self.score}   HighScore :{self.high_score}", move = False,align = "center",font = ("Verdana",15, "normal"))

    def increaseScore(self):
        self.score += 1
        self.update()

    def resetScore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode = "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update()





    