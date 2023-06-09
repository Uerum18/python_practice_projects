from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = -1
        self.increment_score()

    def increment_score(self):
        self.clear()
        self.score += 1
        self.color('cyan')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)