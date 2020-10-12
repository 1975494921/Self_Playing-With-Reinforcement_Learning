from func import *
import time
from Parameters import *
from screen import Display
import platform
import os

FRESH_TIME = 0.1
clear_command = ''
Greedy_Policy = False
Greedy_Factor = 0.9

# q_table: x represent column, y represent row,(x,y,action)
global q_table


def Moving_Show():
    while True:
        step_counter = 0
        S_x = Robot_init_X
        S_y = Robot_init_Y
        Display(S_x, S_y, clear_command)
        is_terminated = False
        while not is_terminated:
            Act_name, Act_index = choose_action(S_x, S_y, q_table, Greedy_Factor, greedy=Greedy_Policy)
            S_x_, S_y_, R, Terminate, tag = get_env_feedback(S_x, S_y, Act_name)
            if Terminate:
                is_terminated = True

            S_x = S_x_
            S_y = S_y_
            step_counter += 1
            Display(S_x, S_y, clear_command)
            time.sleep(FRESH_TIME)

        print('step:', step_counter, ' ', tag)

        time.sleep(5)


if __name__ == "__main__":
    sys_type = platform.system()
    if sys_type == 'Windows':
        clear_command = 'cls'
    else:
        clear_command = 'clear'

    if os.path.exists('Model.npy'):
        q_table = np.load('Model.npy')
        Moving_Show()
    else:
        print('Model Not Existed')