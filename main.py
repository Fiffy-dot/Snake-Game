# this is the main file for the snake game
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor("black")

# turn off what's happening behind the scenes
screen.tracer(0)

# initiate the snake, food, scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# listen to what the player is pressing
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# start game
game_on = True
# move the snake
while game_on:
    screen.update()
    time.sleep(0.1)  # update the screen to begin the display
    snake.move()

    # detect collision with food
    if snake.head_snake.distance(food) < 15:
        snake.extend()  # adds length to the snake after it eats
        food.refresh()
        score.update_score()

    # detect collision with wall
    if snake.head_snake.xcor() > 290 or snake.head_snake.xcor() < -290 or snake.head_snake.ycor() > 290 or snake.head_snake.ycor() < -290:
        score.game_over()
        game_on = False

    # detect collision with tail
    for bit in snake.snake_bits[1:]:  # to avoid comparing the snake head with itself
        if snake.head_snake.distance(bit) < 10:
            score.game_over()
            game_on = False

screen.exitonclick()
