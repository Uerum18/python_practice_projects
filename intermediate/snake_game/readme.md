# Snake Game

This is a simple implementation of the classic Snake Game using the turtle module in Python.

## How to Play

1. Run the `main.py` file to start the game.
2. Control the snake using the arrow keys (Up, Down, Left, Right) to navigate and eat the food.
3. The objective is to eat as much food as possible without colliding with the boundaries of the game window or the snake's own body.
4. The game ends when the snake hits a boundary or collides with itself.
5. Your score will be displayed at the top of the game window.

## Files

### `main.py`

This file is the main entry point of the game. It sets up the game window, creates instances of the `Snake`, `Food`, and `ScoreBoard` classes, and handles the game logic.

### `snake.py`

This file contains the `Snake` class, which represents the snake in the game. It handles the movement of the snake, adding segments to the snake's body, and changing the snake's direction based on user input.

### `food.py`

This file contains the `Food` class, which represents the food that the snake needs to eat. It handles the appearance and positioning of the food within the game window.

### `score.py`

This file contains the `ScoreBoard` class, which keeps track of the player's score and displays it on the screen. It also displays a "GAME OVER" message when the game ends.

## Dependencies

The game requires the `turtle` module, which is included in the Python standard library.

## Running the Game

To run the game, make sure you have Python installed. Then, execute the following command in your terminal or command prompt:

```
python main.py
```

## Acknowledgements

This project was created as a simple implementation of the Snake Game using Python and the turtle module. It serves as a learning exercise and can be customized or expanded upon as desired.
