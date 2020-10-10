import os
from Parameters import *

def display(x,y,Size_X,Size_Y,Trea_X,Trea_Y,command):
    text =''
    os.system(command)
    for i in range(Size_Y):
        for j in range(Size_X):
            if ((x == j) and (y ==i)):
                text +='O '
            elif ((Trea_X == j) and (Trea_Y == i)):
                text += 'T '

            elif (((j == Bomb1_x) and (i == Bomb1_y)) or ((j == Bomb2_x) and (i == Bomb2_y))):
                text += 'X '

            else:
                text += '_ '
        text += '\n'
    print(text)
