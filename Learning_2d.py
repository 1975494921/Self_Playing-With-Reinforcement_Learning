from func import *
import time
from table_show import print_table
from Parameters import *
from screen import Display
import platform
import os

Load_And_Save_Model = False
FRESH_TIME = 0.05
clear_command = ''
Greedy_Policy = True


# q_table: x represent column, y represent row,(x,y,action)
global q_table


def Reinforcement_Learning():
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S_x = Robot_init_X
        S_y = Robot_init_Y
        Display(S_x, S_y, clear_command)
        is_terminated = False
        while not is_terminated:
            Act_name, Act_index = choose_action(S_x, S_y, q_table, greedy=Greedy_Policy)
            S_x_, S_y_, R, Terminate, tag = get_env_feedback(S_x, S_y, Act_name)
            q_predict = q_table[S_x, S_y, Act_index]
            if Terminate:
                q_target = R
                is_terminated = True
            else:
                q_target = R + GAMMA * np.max(q_table[S_x_, S_y_, :])

            q_table[S_x, S_y, Act_index] += Lr * (q_target - q_predict)
            S_x = S_x_
            S_y = S_y_
            step_counter += 1
            Display(S_x, S_y, clear_command)
            time.sleep(FRESH_TIME)

        print('step:', step_counter, ' ', tag)

        if episode % 10 == 0:  # save model when training for ten times
            if Load_And_Save_Model:
                np.save('Model.npy', q_table)

        time.sleep(3)

        # print_table(q_table)


if __name__ == "__main__":
    sys_type = platform.system()
    if sys_type == 'Windows':
        clear_command = 'cls'
    else:
        clear_command = 'clear'

    if Load_And_Save_Model:
        if os.path.exists('Model.npy'):
            q_table = np.load('Model.npy')
        else:
            q_table = build_q_table()
    else:
        q_table = build_q_table()

    Reinforcement_Learning()
