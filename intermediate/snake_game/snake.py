from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((i * -20, 0))

    def __len__(self):
        return len(self.snake_body)

    def snake_move(self):
        for s in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[s - 1].xcor()
            new_y = self.snake_body[s - 1].ycor()
            self.snake_body[s].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
