# Created with the help of the following github
# https://github.com/curiousily/curiousily.github.com/blob/master/notebooks/rl_fundamentals/2.solving_your_first_mdp.ipynb

from gridworld import create_grid_world, print_grid
from state import State
import numpy as np
import random
import utils


###################
# The environment #
###################
grid_world, car_position = create_grid_world()

###############
# The actions #
###############
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ACTIONS = [UP, DOWN, LEFT, RIGHT]

####################
# Create the State #
####################
start_state = State(grid=grid_world, car_pos=car_position)
random.seed(42) # for reproducibility

N_EPISODES = # TODO how many attempts would it take for the agent to learn?
MAX_STEPS_PER_EPISODE = # TODO after how many attempts should we give up waiting for the agent to learn?
MIN_ALPHA = 0.02
alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)
GAMMA = # TODO how much should the discount factor be?
EPS = # TODO how much should the exploitation factor be?

q_table = dict()

def choose_action(ACTIONS, state): 
    if random.uniform(0, 1) < EPS:
        return random.choice(ACTIONS) 
    else:
        return np.argmax(utils.q(q_table, ACTIONS, state))

#############
# Solve MDP #
#############
for e in range(N_EPISODES):
    
    state = start_state
    total_reward = 0
    ALPHA = alphas[e]

    for _ in range(MAX_STEPS_PER_EPISODE):
        
        action = choose_action(ACTIONS, state)
        next_state, reward, done = utils.act(state, action)
        total_reward += reward
        
        ##################
        # Update Q-Table #
        ##################
        utils.q(q_table, ACTIONS, state)[action] = utils.q(q_table, ACTIONS, state, action) + \
                ALPHA * (reward + GAMMA *  np.max(utils.q(q_table, ACTIONS, next_state)) - utils.q(q_table, ACTIONS, state, action))
        
        # Update current state
        state = next_state

        # Check if game is over #
        if done:
            break
    print(f"Episode {e + 1}: total reward -> {total_reward}")


#####################
# Solve the problem #
#####################
done = False
my_state = start_state
counter = 0
while not done:
    
    print_grid(my_state.grid)

    sa = utils.q(q_table, ACTIONS, my_state)
    my_action = np.argmax(sa)
    my_state, reward, done = utils.act(my_state, my_action)

    counter += 1
    if counter > 15: break

print_grid(my_state.grid)
if counter > 15: print('Your agent has probably entered a loop and will not be able to complete the game. Aborting mission.')

################
# What I learn #
################
print()
i = 0
for row in q_table:
    print(f'State {i}:\tReward {sum(q_table[row])}')
    i += 1
