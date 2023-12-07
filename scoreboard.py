from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide arrow
        self.penup()
        self.player_1 = 0
        self.player_2 = 0
        self.recreate()

    def recreate(self):
        self.clear()
        
        self.goto(-200, 250)
        self.color("dark green")
        self.write(f"Player 1: {self.player_1}", align="center", font=("Courier", 15, "bold"))

        self.goto(200, 250)
        self.color("lime green")
        self.write(f"Player 2: {self.player_2}", align="center", font=("Courier", 15, "bold"))

    # Increase score
    def increase_1(self):
        self.player_1 += 1
        self.recreate()

    def increase_2(self):
        self.player_2 += 1
        self.recreate()