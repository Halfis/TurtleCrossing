from turtle import Turtle, colormode

import random

colormode(255) # Implementing RGB

class CarCreator:
    def __init__(self):
        self.all_cars = [] # List of the cars
        
        
    def create_cars(self):
        random_number = random.randint(1, 10) # Density of cars
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Random color
            new_car.goto(300, random.randint(-200, 200)) # Random position
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(10)