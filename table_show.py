from Parameters import *


def print_table(table):
    print('                 left    right    up    down')
    for x in range(Board_Size_X):
        for y in range(Board_Size_Y):
            print('(', x, ',', y, '):    ', end='')
            for act in range(len(ACTIONS)):
                print(table[x, y, act], '     ', end='')
            print('')