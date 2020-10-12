from Parameters import *
from Bomb import *

text = ''
text += '   '
for v in range(Board_Size_X):
    text += str(v) + ' '

text += '\n'

for i in range(Board_Size_Y):
    if i < 10:
        text += '0' + str(i) + ' '
    else:
        text += str(i) + ' '
    for j in range(Board_Size_X):
        drawed = False
        while not drawed:
            if (j == Treasure_X) and (i == Treasure_Y):
                text += 'T '
                drawed = True

            for v in range(Bomb_Num):
                if (j == Bomb_List[v].X) and (i == Bomb_List[v].Y):
                    text += 'X '
                    drawed = True
                    break

            if not drawed:
                text += '_ '
                drawed = True

            if j >= 10:
                text += ' '
    text += '\n'

print(text)
