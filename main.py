import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("collided")
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 260:
        player.refresh()
        scoreboard.increase_score()
        car_manager.level_up()

screen.exitonclick()
