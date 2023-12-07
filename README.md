# TurtleCrossing

## Description
TurtleCrossing is a simple Python game that represents a duel between two players who compete to get their turtles to the other side of the screen. The players have to avoid cars coming from the side.

## Files

### crossing.py

The main file containing the executable code for the game. Here, the game environment, players, vehicles, and score are initialized.

### player.py

Module with the player's implementation, defining the turtle's movement, position restart, and initialization.

### car_creator.py

Module for creating cars that move across the screen. It also includes code for randomly choosing the car's position and color.

### scoreboard.py

Module for keeping track of player scores. It ensures monitoring and increasing the scores of both players.

## How to Play
1. Run the `crossing.py` file to start the game.
2. Player 1 controls their turtle using the keys `W`, `A`, `D`, `S`.
3. Player 2 controls their turtle using the `Up`, `Down`, `Left`, `Right` arrow keys.
4. The goal is to get the turtle to the other side of the screen.
5. Avoid cars moving from the side to prevent collisions.
6. The scores of both players are displayed on the screen.
