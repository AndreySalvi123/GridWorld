ZOMBIE = "z"
CAR = "c"
ICE_CREAM = "i"
EMPTY = "*"
ZOMBIE_CAR = "zc"
ICE_CREAM_CAR = "ic"

ITEMS = {
    ZOMBIE: 'ZOMBIE', 
    CAR: 'CAR', 
    ICE_CREAM: 'ICE_CREAM', 
    EMPTY: '',
    ZOMBIE_CAR : 'YOU DIE',
    ICE_CREAM_CAR: 'YOU WIN'
}

'''
    Create the environment
'''
def create_grid_world():

    grid = [
        [ZOMBIE, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, ZOMBIE, ZOMBIE, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, ICE_CREAM],
        [CAR, ZOMBIE, EMPTY, ZOMBIE, EMPTY]
    ]

    car_position = [4, 0]
    return grid, car_position

'''
    Make the movement of the zombies
'''
def update_zombies(grid):
    if grid[0][0] == ZOMBIE:
        grid[0][0] = EMPTY
        if grid[1][0] == EMPTY: grid[1][0] = ZOMBIE
        else: grid[1][0] += ZOMBIE
    else:
        grid[1][0] = EMPTY
        if grid[0][0] == EMPTY: grid[0][0] = ZOMBIE
        else: grid[0][0] += ZOMBIE


    if grid[1][2] == ZOMBIE:
        grid[1][2] = EMPTY
        if grid[2][2] == EMPTY: grid[2][2] = ZOMBIE
        else: grid[2][2] += ZOMBIE
    else:
        grid[2][2] = EMPTY
        if grid[1][2] == EMPTY: grid[1][2] = ZOMBIE
        else: grid[1][2] += ZOMBIE


    if grid[4][1] == ZOMBIE:
        grid[4][1] = EMPTY
        if grid[3][1] == EMPTY: grid[3][1] = ZOMBIE
        else: grid[3][1] += ZOMBIE
    else:
        grid[3][1] = EMPTY
        if grid[4][1] == EMPTY: grid[4][1] = ZOMBIE
        else: grid[4][1] += ZOMBIE


    if grid[4][3] == ZOMBIE:
        grid[4][3] = EMPTY
        if grid[3][3] == EMPTY: grid[3][3] = ZOMBIE
        else: grid[3][3] += ZOMBIE
    else:
        grid[3][3] = EMPTY
        if grid[4][3] == EMPTY: grid[4][3] = ZOMBIE
        else: grid[4][3] += ZOMBIE


'''
    Print the GridWorld
'''
def print_grid(grid):
    horizontal_wall = ('%10s' * 10) % ('----------', '----------', '----------', '----------', '----------', '----------', '----------', '----------', '----------', '----------')
    print(horizontal_wall)
    for line in grid:
        s = ('%10s' * 10) % (ITEMS[line[0]], '|', ITEMS[line[1]], '|', ITEMS[line[2]], '|', ITEMS[line[3]], '|', ITEMS[line[4]], '|')
        print(s)
        print(horizontal_wall)
    print('\n\n')