from turtle import Screen
from player import Player
from car_creator import CarCreator
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0) # Hiding movement of players to start location

player_1 = Player((-10, -280), "dark green")
player_2 = Player((10, -280), "lime green")
cars = CarCreator()
scoreboard = Scoreboard()

screen.listen() # listening to key inputs

screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_left, "a")
screen.onkey(player_1.move_right, "d")
screen.onkey(player_1.move_down, "s")

screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_left, "Left")
screen.onkey(player_2.move_right, "Right")
screen.onkey(player_2.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_cars()
    cars.move()

    screen.update() # Players are visible now
    
    for car in cars.all_cars:
        if player_1.distance(car)<20:
            player_1.restart()
        if player_2.distance(car)<20:
            player_2.restart()
            
    # Winning conditions    
    if player_1.ycor() > 230:
        scoreboard.increase_1()
        player_1.restart()
        player_2.restart()
    if player_2.ycor() > 230:
        scoreboard.increase_2()
        player_1.restart()
        player_2.restart()

screen.exitonclick()