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
    alive_indices = []
    user_friendly_world = []
    for x in range(0, len(world)):
        print(world[x])
        row = []
        for y in range(0, len(world[x])):
            if world[x][y]:
              row.append("X("+str(x)+","+str(y)+")")
              alive_indices.append((x,y))
            else:
              # row.append("("+str(x)+","+str(y)+")")
              row.append(" ")
        user_friendly_world.append(row)
    print("User friendly world: Generation =", generation)
    for x in range(0, len(user_friendly_world)):
        for y in range(0, len(user_friendly_world[x])):
            print("%8s|" % user_friendly_world[x][y], end="")
        print("")
        # print(user_friendly_world[x])
    print("Alive indices: Generation =", generation)
    print(alive_indices)
    

def get_live_neighbours_count(x, y):
    global world
    count = 0
    if x < len(world) and y < len(world[x]):
        # left and right squares
        if y-1 >= 0 and world[x][y-1]:
            count += 1
        if y+1 < len(world[x]) and world[x][y+1]:
            count += 1

        # top and bottom squares
        if x-1 >= 0 and world[x-1][y]:
            count += 1
        if x+1 < len(world) and world[x+1][y]:
            count += 1

        # top left square
        if x-1 >= 0 and y-1 >= 0 and world[x-1][y-1]:
            count += 1

        # top right square
        if x-1 >= 0 and y+1 < len(world[x]) and world[x-1][y+1]:
            count += 1

        # bottom left square
        if x+1 < len(world) and y-1 >= 0 and world[x+1][y-1]:
            count += 1

        # bottom right square
        if x+1 < len(world) and y+1 < len(world[x]) and world[x+1][y+1]:
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

            next_gen_world[x][y] = world[x][y]
            # live cell
            if world[x][y]:
                # 1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation
                if live_neighbours_count < 2:
                    # the cell dies
                    next_gen_world[x][y] = 0
                    input("condition 1 (dies): Any live cell with fewer than two live neighbors dies as if caused by underpopulation: x = " + str(x) + ", y = " + str(y))

                # 2. Any live cell with two or three live neighbors lives on to the next generation.
                elif live_neighbours_count == 2 or live_neighbours_count == 3:
                    # the cell lives
                    next_gen_world[x][y] = 1
                    input("condition 2 (lives): Any live cell with two or three live neighbors lives on to the next generation: x = " + str(x) + ", y = " + str(y))

                # 3. Any live cell with more than three live neighbors dies, as if by overcrowding.
                elif live_neighbours_count > 3:
                    # the cell dies
                    next_gen_world[x][y] = 0
                    input("condition 3 (dies): Any live cell with more than three live neighbors dies, as if by overcrowding: x = " + str(x) + ", y = " + str(y))
            # dead cell
            else:
                # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
               if live_neighbours_count == 3:
                    # the cell lives
                    next_gen_world[x][y] = 1
                    input("condition 4 (lives): Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction: x = " + str(x) + ", y = " + str(y))

    return next_gen_world


def tick():
    global world, generation_number
    generation_number += 1
    world = populate_next_gen_world()
    print("generation number = ", generation_number)
    print_world(generation_number)

#initialize_world_random(5)
initialize_world()
print_world(0)
keep_ticking = True
while(keep_ticking):
    answer = input("Keep ticking (Y/n) :")
    if answer.lower().startswith("n"):
        keep_ticking = False
    else:
        tick()

