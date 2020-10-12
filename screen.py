import os
from Parameters import *
from Bomb import *


def Display(x, y, command):
    text = ''
    os.system(command)
    for i in range(Board_Size_Y):
        for j in range(Board_Size_X):
            drawed = False
            while not drawed:
                if (j == x) and (i == y):
                    text += 'O '
                    drawed = True
                    continue

                if (j == Treasure_X) and (i == Treasure_Y):
                    text += 'T '
                    drawed = True
                    continue

                for v in range(Bomb_Num):
                    if (j == Bomb_List[v].X) and (i == Bomb_List[v].Y):
                        text += 'X '
                        drawed = True
                        break

                if not drawed:
                    text += '_ '
                    drawed = True

        text += '\n'
    print(text)
