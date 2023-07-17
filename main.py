from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import random



screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,  "Down")
screen.onkey(snake.left,  "Left")
screen.onkey(snake.right,  "Right")

SCREEN_X_POS = int(screen.window_width() / 2)
SCREEN_X_NEG = -int(screen.window_width() / 2)
SCREEN_Y_POS = int(screen.window_height() / 2)
SCREEN_Y_NEG = -int(screen.window_height() / 2)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect colision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        score_board.clear()
        score_board.score_tracking()
        score_board.position()
        snake.add_segment()

    if snake.head.xcor() > SCREEN_X_POS or\
            snake.head.xcor() < SCREEN_X_NEG or\
            snake.head.ycor() > SCREEN_Y_POS or\
            snake.head.ycor() < SCREEN_Y_NEG:
        game_is_on = False
        score_board.game_over()

    #Detect collision with tail.
    for segment in snake.snake[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()



screen.exitonclick()




















#print(snake[2].xcor())

# starting_positions =[(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)
#     snake.append(new_segment)

