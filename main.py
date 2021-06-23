#!/usr/bin/env python3
from random import seed
from random import randint

generation_number = 0
world = None
world_size = 25

def empty_world(world_size):
    w = []
    for x in range(0, world_size):
        row = []
        for y in range(0, world_size):
            row.append(0)
        w.append(row)

    return w

# populate world with random cells
def initialize_world():
    global world
    world = empty_world(world_size)
    # initial values
    world[12][13] = 1
    world[13][14] = 1
    world[14][12] = 1
    world[14][13] = 1
    world[14][14] = 1
    print_world(0)

# populate world with random cells
def initialize_world_random():
    global world
    world = []
    seed(100)
    for x in range(0, world_size):
        row = []
        for y in range(0, world_size):
            row.append(randint(0, 100) % 2)
        world.append(row)
    print_world(0)


def print_world(generation):
    global world
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
    print("User friendly world: Generation =", generation)
    for x in range(0, len(user_friendly_world)):
        print(user_friendly_world[x])
    

def get_live_neighbours_count(x, y):
    global world
    count = 0
    # left and right squares
    if world[x][y-1]:
        count += 1
    if world[x][y+1]:
        count += 1

    # top and bottom squares
    if world[x-1][y]:
        count += 1
    if world[x+1][y]:
        count += 1

    # top left square
    if world[x-1][y-1]:
        count += 1

    # top right square
    if world[x-1][y+1]:
        count += 1

    # bottom left square
    if world[x+1][y-1]:
        count += 1

    # bottom right square
    if world[x+1][y+1]:
        count += 1

    return count

def populate_next_gen_world():
    global world
    x, y = 0, 0
    print("x =", x, "y =", y)
    next_gen_world = empty_world(world_size)
    for x in range(0, len(world)):
        for y in range(0, len(world[x])):
            live_neighbours_count = get_live_neighbours_count(x, y)

            # live cell
            if world[x][y]:
                # 1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation
                if live_neighbours_count < 2:
                    # the cell dies
                    next_gen_world[x][y] = 0

                # 2. Any live cell with two or three live neighbors lives on to the next generation.
                elif live_neighbours_count == 2 or live_neighbours_count == 3:
                    # the cell lives
                    next_gen_world[x][y] = 1

                # 3. Any live cell with more than three live neighbors dies, as if by overcrowding.
                elif live_neighbours_count > 3:
                    # the cell dies
                    next_gen_world[x][y] = 0
            # dead cell
            else:
                # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
               if live_neighbours_count == 3:
                    # the cell lives
                    next_gen_world[x][y] = 1

    return next_gen_world


def tick():
    global world, generation_number
    generation_number += 1
    world = populate_next_gen_world()
    print("generation number = ", generation_number)
    print_world(generation_number)

#initialize_world_random(5)
initialize_world()
keep_ticking = True
while(keep_ticking):
    tick()
    answer = input("Keep ticking (Y/n) :")
    if answer.lower().startswith("n"):
        keep_ticking = False


