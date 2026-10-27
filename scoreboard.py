from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_center_line()
        # Left Player Score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        # Right Player Score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def draw_center_line(self):
        line = Turtle()
        line.color("white")
        line.penup()
        line.goto(0, -300)
        line.setheading(90)
        line.hideturtle()
        line.pensize(3)
        while line.ycor() < 300:
            line.pendown()
            line.forward(15)
            line.penup()
            line.forward(15)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()