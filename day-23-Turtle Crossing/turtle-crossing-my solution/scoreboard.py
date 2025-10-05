from turtle import Turtle

FONT = ("Courier", 24, "normal")


# Screen:
# 1. showing what level the player is at, "Level: 1"
# 2. automatically refresh the screen to show the next level
# 3. showing "GAME OVER"

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.level = Turtle()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        # self.write_score()

    # def write_score(self, prev_level):
    #     self.increase_score(prev_level)
    #     self.write(f"Level {self.level_num}", align="left", font=FONT)


    def update_score(self, current_level):
        self.increase_score(current_level)
        self.clear()
        self.write(f"Level {self.level_num}", align="left", font=FONT)

    def increase_score(self, current_level):
        self.level_num +=  current_level
        return self.level_num

    def game_over(self):
        self.goto(0, 0)
        # self.clear()
        self.write(f"GAME OVER", align = "center", font = FONT)
