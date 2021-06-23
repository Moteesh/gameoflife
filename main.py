#!/usr/bin/env python3
from random import seed
from random import randint

generation_number = 0
world = None
user_friendly_world = None

# populate world with random cells
def initialize_world():
    global world, user_friendly_world
    size = 25
    world = []
    user_friendly_world = []
    seed(100)
    for x in range(0, size):
        row = []
        user_friendly_row = []
        for y in range(0, size):
            row.append(0)
            user_friendly_row.append("D")
        world.append(row)
        user_friendly_world.append(user_friendly_row)
    # initial values
    world[12][13] = 1
    user_friendly_world[12][13] = "A"
    world[13][14] = 1
    user_friendly_world[13][14] = "A"
    world[14][12] = 1
    user_friendly_world[14][12] = "A"
    world[14][13] = 1
    user_friendly_world[14][13] = "A"
    world[14][14] = 1
    user_friendly_world[14][14] = "A"
    print_world()

# populate world with random cells
def initialize_world_random(size):
    global world
    world = []
    seed(100)
    for x in range(0, size):
        row = []
        for y in range(0, size):
            row.append(randint(0, 100) % 2)
        world.append(row)
    print_world()


def print_world():
    global world, user_friendly_world
    user_friendly_world = []
    for x in range(0, len(world)):
        print(world[x])
        row = []
        for y in range(0, len(world[x])):
            if world[x][y]:
              row.append("A")
            else:
              row.append("D")
        user_friendly_world.append(row)
    print("User friendly world:")
    for x in range(0, len(user_friendly_world)):
        print(user_friendly_world[x])
    

def populate_world():
    x, y = 0, 0
    print("x =", x, "y =", y)
    

def tick():
    global generation_number
    generation_number += 1
    print("ticked, generation number = ", generation_number)
    populate_world()


#initialize_world_random(5)
initialize_world()
tick()
