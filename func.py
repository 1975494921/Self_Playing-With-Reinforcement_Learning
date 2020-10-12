import numpy as np
from Parameters import *
from Bomb import *

def build_q_table():
    table = np.zeros((Board_Size_X, Board_Size_Y, len(ACTIONS)))
    return table


def choose_action(state_x, state_y, q_table, greedy_factor, greedy=True):
    state_actions = q_table[state_x, state_y, :]
    if ((np.random.uniform() > greedy_factor) and greedy) or ((state_actions <= 0).all()):
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

    else:
        for k in range(Bomb_Num):
            if (S_x_ == Bomb_List[k].X) and (S_y_ == Bomb_List[k].Y):
                if Bomb_List[k].Enable:
                    Terminate = True
                    tag = 'Lost'
                    R = -1
                    break

    return S_x_, S_y_, R, Terminate, tag
