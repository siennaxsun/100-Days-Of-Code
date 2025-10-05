from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-10, 260)
        self.color("white")
        self.update_score()
        self.reset()

    def update_score(self):
        # self.goto(-100, 260)
        self.clear()  # clear what's previously on the screen
        self.write(f"Scores: {self.score}    High Score: {self.high_score}", align="center", font=('Arial', 18,
                                                                                                  'normal'))

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()
        return self.score


    #
    # def game_over(self):
    #     self.goto(-10, 0)
    #     self.write(f"Game Over", align="center", font=('Arial', 18, 'normal'))
    #
    # def highest_score(self):
    #     self.goto(100, 260)
    #     self.clear()
    #     self.write(f"High Score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))
    #     # return self.highest_score



    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        return self.high_score

