import numpy as np
import random
from Parameters import *


def build_q_table(x_size, y_size, actions):
    table = np.zeros((x_size, y_size, len(actions)))
    return table


def choose_action(state_x, state_y, q_table, actions, Epsilon, greedy=True, ):
    state_actions = q_table[state_x, state_y, :]
    if ((np.random.uniform() > Epsilon) and (greedy == True)) or ((state_actions == 0).all()):
        action_index = random.randint(0, len(actions) - 1)
        action_name = actions[action_index]
    else:
        action_index = np.argmax(state_actions)
        action_name = actions[action_index]
    return action_name, action_index


def get_env_feedback(S_x, S_y, Act_name, x_size, y_size, trea_x, trea_y):
    R = 0
    Terminate = False
    if Act_name == 'right':  # move right
        if S_x == x_size - 1:  # reach the right wall
            S_x_ = S_x
            S_y_ = S_y
        else:
            S_x_ = S_x + 1
            S_y_ = S_y

    elif Act_name == 'left':  # move left
        if S_x == 0:  # reach the left wall
            S_x_ = S_x
            S_y_ = S_y
        else:
            S_x_ = S_x - 1
            S_y_ = S_y

    elif Act_name == 'up':  # move up
        if S_y == 0:  # reach the top wall
            S_x_ = S_x
            S_y_ = S_y
        else:
            S_x_ = S_x
            S_y_ = S_y - 1

    elif Act_name == 'down':  # move down
        if S_y == y_size - 1:  # reach the bottom wall
            S_x_ = S_x
            S_y_ = S_y
        else:
            S_x_ = S_x
            S_y_ = S_y + 1

    if (S_x_ == trea_x) and (S_y_ == trea_y):
        Terminate = True
        R = 1

    if ((S_x_ == Bomb1_x) and (S_y_ == Bomb1_y)) or ((S_x_ == Bomb2_x) and (S_y_ == Bomb2_y)):
        Terminate = True
        R = -1

    return S_x_, S_y_, R, Terminate
