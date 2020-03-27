from gridworld import update_zombies
from copy import deepcopy
from state import State
import numpy as np
import random

ZOMBIE = "z"
CAR = "c"
ICE_CREAM = "i"
EMPTY = "*"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

"""
    Perform an action
    Returns the reward, the new state, and if the game is over
"""
def act(state, action):
        
    p = new_car_pos(state, action)
    
    grid_item = state.grid[p[0]][p[1]]
    
    new_grid = deepcopy(state.grid)
    
    if grid_item == ZOMBIE:
        reward = # TODO how much should be the reward if we are killed by the zombie?
        is_done = True
        old = state.car_pos
        new_grid[old[0]][old[1]] = EMPTY
        is_done = True
        new_grid[p[0]][p[1]] += CAR
    
    elif grid_item == ICE_CREAM:
        reward = # TODO how much should be the reward if we win the game?
        old = state.car_pos
        new_grid[old[0]][old[1]] = EMPTY
        is_done = True
        new_grid[p[0]][p[1]] += CAR
        
    elif grid_item == EMPTY:
        reward = # TODO how much should be the reward if we still alive?
        is_done = False
        old = state.car_pos
        new_grid[old[0]][old[1]] = EMPTY
        new_grid[p[0]][p[1]] = CAR

    elif grid_item == CAR:
        reward = # TODO how much should the reward be if we hit the head on the wall?
        is_done = False

    else:
        raise ValueError(f"Unknown grid item {grid_item}")
    
    update_zombies(new_grid)
    if new_grid[p[0]][p[1]] in ['cz', 'zc']: 
        reward = # TODO how much should be the reward if we are killed by the zombie?
        is_done = True
    
    st = State(grid=new_grid, car_pos=p)

    return st, reward, is_done

'''
    Computes the position car after the action. 
    Is the Transition Function
'''
def new_car_pos(state, action):

    p = deepcopy(state.car_pos)
    if action == UP:
        p[0] = max(0, p[0] - 1)
    elif action == DOWN:
        p[0] = min(len(state.grid) - 1, p[0] + 1)
    elif action == LEFT:
        p[1] = max(0, p[1] - 1)
    elif action == RIGHT:
        p[1] = min(len(state.grid[0]) - 1, p[1] + 1)
    else:
        raise ValueError(f"Unknown action {action}")
    return p


"""
    Returns the Q quality by a gived state and action
"""
def q(q_table, ACTIONS, state, action=None):
    
    if state not in q_table:
        q_table[state] = np.zeros(len(ACTIONS))
        
    if action is None:
        return q_table[state]
    
    return q_table[state][action]