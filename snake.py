from turtle import Turtle, Screen
MOVE_INSTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for x in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            if len(self.snake) > 0:
                new_turtle.goto(x=(self.snake[x - 1].xcor() - 20), y=0)
            new_turtle.color("white")
            self.snake.append(new_turtle)

    def add_segment(self):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.goto(x=(self.snake[-1].xcor()), y=self.snake[-1].ycor())
        new_turtle.color("white")
        self.snake.append(new_turtle)


    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_INSTANCE)

    def up(self):
        if self.head.heading() != DOWN:
             self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)