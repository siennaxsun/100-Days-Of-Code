from turtle import Turtle


ALIGNMENT = "right"
FONT = ('Arial', 40, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.final_score = 0
        self.score(pos_x)
        # self.write_score(pos_x)
        # self.score_update(pos_x)

    def score(self, pos_x):
        score = Turtle()
        score.hideturtle()
        score.color ("white")
        score.penup()
        score.goto(pos_x, 240)
        self.write(f"{self.final_score}", align=ALIGNMENT, font=FONT)

    # def write_score(self, pos_x):
    #     self.score(pos_x)
    #     self.write(f"{self.final_score}", align=ALIGNMENT, font=FONT)


    def score_update(self, pos_x):
       self.final_score += 1
       self.clear()
       # self.write(f"{self.final_score}", align=ALIGNMENT, font=FONT)
       self.score(pos_x)
       # note if you just a the line of self.write(f-string), the scoreboard will not showing up
       # you have to use the function self.score() because this function not just includes the write
       # part, but also the turtle part, which you will need to show up the score

       # self.write_score(pos_x)
