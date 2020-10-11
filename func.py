import numpy as np
from Parameters import *


def build_q_table():
    table = np.zeros((Board_Size_X, Board_Size_Y, len(ACTIONS)))
    return table


def choose_action(state_x, state_y, q_table, greedy=True):
    state_actions = q_table[state_x, state_y, :]
    if ((np.random.uniform() > EPSILON) and greedy) or ((state_actions <= 0).all()):
        action_index = np.random.randint(0, len(ACTIONS))
        while state_actions[action_index] < 0:  # avoid doing error moves
            action_index = np.random.randint(0, len(ACTIONS))

        action_name = ACTIONS[action_index]

    else:
        action_index = np.argmax(state_actions)
        action_name = ACTIONS[action_index]
    return action_name, action_index


def get_env_feedback(S_x, S_y, Act_name):
    R = 0
    tag = ''
    Terminate = False
    if Act_name == 'right':  # move right
        if S_x == Board_Size_X - 1:  # reach the right wall
            S_x_ = S_x
            S_y_ = S_y
            R = -0.2
        else:
            S_x_ = S_x + 1
            S_y_ = S_y

    elif Act_name == 'left':  # move left
        if S_x == 0:  # reach the left wall
            S_x_ = S_x
            S_y_ = S_y
            R = -0.2
        else:
            S_x_ = S_x - 1
            S_y_ = S_y

    elif Act_name == 'up':  # move up
        if S_y == 0:  # reach the top wall
            S_x_ = S_x
            S_y_ = S_y
            R = -0.2
        else:
            S_x_ = S_x
            S_y_ = S_y - 1

    elif Act_name == 'down':  # move down
        if S_y == Board_Size_Y - 1:  # reach the bottom wall
            S_x_ = S_x
            S_y_ = S_y
            R = -0.2
        else:
            S_x_ = S_x
            S_y_ = S_y + 1

    if (S_x_ == Treasure_X) and (S_y_ == Treasure_Y):  # find treasure
        Terminate = True
        tag = 'Win'
        R = 1

    elif (S_x_ == Bomb1_x) and (S_y_ == Bomb1_y):
        if Bomb1_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb2_x) and (S_y_ == Bomb2_y):
        if Bomb2_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb3_x) and (S_y_ == Bomb3_y):
        if Bomb3_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb4_x) and (S_y_ == Bomb4_y):
        if Bomb4_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb5_x) and (S_y_ == Bomb5_y):
        if Bomb5_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb6_x) and (S_y_ == Bomb6_y):
        if Bomb6_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb7_x) and (S_y_ == Bomb7_y):
        if Bomb7_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb8_x) and (S_y_ == Bomb8_y):
        if Bomb8_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb9_x) and (S_y_ == Bomb9_y):
        if Bomb9_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    elif (S_x_ == Bomb10_x) and (S_y_ == Bomb10_y):
        if Bomb10_Enable:
            Terminate = True
            tag = 'Lost'
            R = -1

    return S_x_, S_y_, R, Terminate, tag
