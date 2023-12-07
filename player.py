from turtle import Turtle

class Player(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("turtle")
        self.setheading(90) # Rotation of player
        self.penup(); # Not making line when moving
        self.color(color)
        self.start_position = position
        self.goto(self.start_position)
        
    
    # Movement
    def move_up(self):
        self.setheading(90)
        self.forward(10)
        
    def move_left(self):
        self.setheading(-180)
        self.forward(10)
        
    def move_right(self):
        self.setheading(0)
        self.forward(10)
        
    def move_down(self):
        self.setheading(-90)
        self.forward(10)
        
    # Restart
    def restart(self):
        self.goto(self.start_position)