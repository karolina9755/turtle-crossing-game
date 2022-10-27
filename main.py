import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

my_turtle = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkeypress(my_turtle.move, "Up")
screen.onkeypress(my_turtle.move, "space")

game_is_on = True
car_occurence_frequency = 20
i = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if i % car_occurence_frequency == 0:
        new_car = CarManager()
        cars.append(new_car)
        i = 0

    # collision with car
    for car in cars:
        car.move()
        if my_turtle.distance(car) < 20 or my_turtle.distance(car.xcor()+20, car.ycor()) < 20 \
                or my_turtle.distance(car.xcor()-20, car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False
            print(f"turtle: {my_turtle.xcor()}, {my_turtle.ycor()}")
            print(f"car: {car.xcor()}, {car.ycor()}")

    # achieving finish line
    if my_turtle.ycor() > my_turtle.finish:
        scoreboard.increase_level()
        my_turtle.reset()
        car_occurence_frequency = (car_occurence_frequency * 0.9).__ceil__()
        i = 0

    i += 1


screen.exitonclick()
