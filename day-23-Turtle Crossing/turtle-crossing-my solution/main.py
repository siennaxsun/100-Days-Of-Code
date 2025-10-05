import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



collision_distance = 35
current_level = 0
prev_level = 0
car_count = random.randint(5, 20)
game_begin = True


# create many cars
def car_pool(car_count):
    car_pool = []
    for i in range(0, car_count):
        car = CarManager()
        # car.moving()
        car_pool.append(car)
    return car_pool

def refresh_car_moving_screen(current_level, prev_level):
    # car moving forward at a certain speed at level 1
    for car in cars:
        car.move(current_level, prev_level)

def detect_collision(cars, player):
    for car in cars:
        for segment in car.segments:
            if player.distance(segment) < collision_distance:
                return True



while game_begin:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # create a new car pool
    cars = car_pool(car_count)

    # create a new turtle player
    tim = Player()

    # create a score board showing what level the player is at
    score = Scoreboard()
    score.update_score(current_level)
    dists = []
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        refresh_car_moving_screen(current_level, prev_level)

        tim_position = tim.screen_listening()
        print ("tim's y position is: " + str(tim_position))

        # if turtle passing the certain y shreshould, it wins this level and moves to next level
        if tim_position > 250:
            # level up: update the screen to next level
            prev_level = current_level
            current_level += 1

            # refresh the car pool and car moving, car moves faster
            game_is_on = False
            screen.clear()


        # check if the turtle hits a car: if it does, game over
        for car in cars:
            dist = tim.distance(car.head)
            dists.append(dist)
            dists.sort()
            print (dists[0], dists[-1])

            if dist < collision_distance:
                print("collision is ------------------- detected")
                score.game_over()
                game_is_on = False


