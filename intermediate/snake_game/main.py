import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
game_is_on = True
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increment_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
