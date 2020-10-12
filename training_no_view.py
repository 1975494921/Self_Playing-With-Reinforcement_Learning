from func import *
from Parameters import *
import os
import platform

Greedy_Policy = True
Greedy_Factor = 0.5
clear_command = ''

# q_table: x represent column, y represent row,(x,y,action)
global q_table


def Reinforcement_Learning():
    epo = 0
    print('training......')
    while True:
        epo += 1
        step_counter = 0
        S_x = Robot_init_X
        S_y = Robot_init_Y
        is_terminated = False
        while not is_terminated:
            Act_name, Act_index = choose_action(S_x, S_y, q_table, Greedy_Factor, greedy=Greedy_Policy)
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

        if epo == 100:
            print('Greedy_Step:', step_counter, ' ', tag)
            np.save('Model.npy', q_table)
            #os.system(clear_command)
            epo = 0


if __name__ == "__main__":
    sys_type = platform.system()
    if sys_type == 'Windows':
        clear_command = 'cls'
    else:
        clear_command = 'clear'

    if os.path.exists('Model.npy'):
        q_table = np.load('Model.npy')
    else:
        q_table = build_q_table()

    Reinforcement_Learning()
