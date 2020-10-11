import os
from Parameters import *


def Display(x, y, command):
    text = ''
    os.system(command)
    for i in range(Board_Size_Y):
        for j in range(Board_Size_X):
            if (j == x) and (i == y):
                text += 'O '

            elif (j == Treasure_X) and (i == Treasure_Y):
                text += 'T '

            elif ((j == Bomb1_x) and (i == Bomb1_y)) and Bomb1_Enable:
                text += 'X '

            elif ((j == Bomb2_x) and (i == Bomb2_y)) and Bomb2_Enable:
                text += 'X '

            elif ((j == Bomb3_x) and (i == Bomb3_y)) and Bomb3_Enable:
                text += 'X '

            elif ((j == Bomb4_x) and (i == Bomb4_y)) and Bomb4_Enable:
                text += 'X '

            elif ((j == Bomb5_x) and (i == Bomb5_y)) and Bomb5_Enable:
                text += 'X '

            elif ((j == Bomb6_x) and (i == Bomb6_y)) and Bomb6_Enable:
                text += 'X '

            elif ((j == Bomb7_x) and (i == Bomb7_y)) and Bomb7_Enable:
                text += 'X '

            elif ((j == Bomb8_x) and (i == Bomb8_y)) and Bomb8_Enable:
                text += 'X '

            elif ((j == Bomb9_x) and (i == Bomb9_y)) and Bomb9_Enable:
                text += 'X '

            elif ((j == Bomb10_x) and (i == Bomb10_y)) and Bomb10_Enable:
                text += 'X '

            else:
                text += '_ '

        text += '\n'
    print(text)
