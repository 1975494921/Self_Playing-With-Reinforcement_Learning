from func import *
import time
from table_show import print_table
from Parameters import *
from screen import display
import platform

Board_Size_X = 8
Board_Size_Y = 8
Trea_X = 6  # start with 0, 0<= Trea_X <= Board_Size_X - 1
Trea_Y = 7  # start with 0, 0<= Trea_Y <= Board_Size_Y - 1
Robot_init_X = 0
Robot_init_Y = 0

clear_command = ''


# q_table: x represent column, y represent row,(x,y,action)

def Reinforcement_Learning():
    q_table = build_q_table(Board_Size_X, Board_Size_Y, ACTIONS)

    for episode in range(MAX_EPISODES):
        step_counter = 0
        S_x = Robot_init_X
        S_y = Robot_init_Y
        display(S_x, S_y, Board_Size_X, Board_Size_Y, Trea_X, Trea_Y, clear_command)
        is_terminated = False
        while not is_terminated:
            Act_name, Act_index = choose_action(S_x, S_y, q_table, ACTIONS, EPSILON, greedy=True)
            S_x_, S_y_, R, Terminate = get_env_feedback(S_x, S_y, Act_name, Board_Size_X, Board_Size_Y, Trea_X, Trea_Y)
            q_predict = q_table[S_x, S_y, Act_index]
            if (Terminate):
                q_target = R
                is_terminated = True
            else:
                q_target = R + GAMMA * np.max(q_table[S_x_, S_y_, :])

            q_table[S_x, S_y, Act_index] += Lr * (q_target - q_predict)
            S_x = S_x_
            S_y = S_y_
            step_counter += 1
            display(S_x, S_y, Board_Size_X, Board_Size_Y, Trea_X, Trea_Y, clear_command)
            time.sleep(FRESH_TIME)

        print('step:', step_counter)
        time.sleep(3)

        # print_table(q_table, ACTIONS,Board_Size_X,Board_Size_Y,Trea_X,Trea_Y)


if __name__ == "__main__":
    sys_type = platform.system()
    if sys_type == 'Windows':
        clear_command = 'cls'
    else:
        clear_command = 'clear'

    Reinforcement_Learning()
