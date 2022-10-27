from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.level = 0
        self.prompt = ""
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.prompt = f"Level: {self.level}"
        self.write(self.prompt, align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    # def game_finished(self):
    #     self.goto(0,0)
    #     self.write("    CONGRATULATIONS!\nYOU'VE FINISHED THE GAME!", align="center", font=FONT)



