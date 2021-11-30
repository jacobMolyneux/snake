from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect food and snake collision
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


screen.exitonclick()
