class Bomb_define(object):
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Enable = False

    def set(self, x, y, enable):
        self.X = x
        self.Y = y
        self.Enable = enable


Bomb_Num = 142
Bomb_List = []
for i in range(Bomb_Num):
    Bomb_List.append(Bomb_define())

Bomb_List[0].set(2, 2, True)
Bomb_List[1].set(1, 0, True)
Bomb_List[2].set(6, 3, True)
Bomb_List[3].set(6, 6, True)
Bomb_List[4].set(4, 5, True)
Bomb_List[5].set(0, 4, True)
Bomb_List[6].set(13, 13, True)
Bomb_List[7].set(10, 3, True)
Bomb_List[8].set(15, 20, True)
Bomb_List[9].set(1, 3, True)
Bomb_List[10].set(3, 4, True)
Bomb_List[11].set(2, 5, True)
Bomb_List[12].set(2, 6, True)
Bomb_List[13].set(4, 7, True)
Bomb_List[14].set(7, 7, True)

Bomb_List[15].set(17, 17, True)
Bomb_List[16].set(18, 18, True)
Bomb_List[17].set(16, 18, True)
Bomb_List[18].set(19, 16, True)
Bomb_List[19].set(16, 19, True)
Bomb_List[20].set(18, 15, True)
Bomb_List[21].set(9, 6, True)
Bomb_List[22].set(10, 7, True)
Bomb_List[23].set(11, 6, True)
Bomb_List[24].set(12, 4, True)
Bomb_List[25].set(13, 5, True)
Bomb_List[26].set(19, 4, True)
Bomb_List[27].set(14, 7, True)
Bomb_List[28].set(3, 10, True)
Bomb_List[29].set(16, 10, True)

Bomb_List[30].set(9, 0, True)
Bomb_List[31].set(8, 1, True)
Bomb_List[32].set(1, 7, True)
Bomb_List[33].set(0, 9, True)
Bomb_List[34].set(5, 8, True)
Bomb_List[35].set(3, 9, True)
Bomb_List[36].set(4, 11, True)
Bomb_List[37].set(5, 12, True)
Bomb_List[38].set(14, 16, True)
Bomb_List[39].set(17, 15, True)

Bomb_List[40].set(22, 22, True)
Bomb_List[41].set(21, 23, True)
Bomb_List[42].set(20, 24, True)
Bomb_List[43].set(23, 20, True)
Bomb_List[44].set(24, 19, True)
Bomb_List[45].set(10, 19, True)
Bomb_List[46].set(21, 20, True)
Bomb_List[47].set(20, 19, True)
Bomb_List[48].set(21, 17, True)
Bomb_List[49].set(22, 16, True)

Bomb_List[50].set(8, 3, True)
Bomb_List[51].set(8, 5, True)
Bomb_List[52].set(11, 2, True)
Bomb_List[53].set(6, 14, True)
Bomb_List[54].set(10, 9, True)
Bomb_List[55].set(22, 10, True)
Bomb_List[56].set(22, 12, True)
Bomb_List[57].set(21, 13, True)
Bomb_List[58].set(24, 9, True)
Bomb_List[59].set(1, 13, True)

Bomb_List[60].set(2, 12, True)
Bomb_List[61].set(0, 11, True)
Bomb_List[62].set(5, 15, True)
Bomb_List[63].set(18, 10, True)
Bomb_List[64].set(11, 10, True)
Bomb_List[65].set(12, 8, True)
Bomb_List[66].set(17, 6, True)
Bomb_List[67].set(7, 13, True)
Bomb_List[68].set(7, 14, True)
Bomb_List[69].set(6, 10, True)

Bomb_List[70].set(20, 14, True)
Bomb_List[71].set(18, 19, True)
Bomb_List[72].set(11, 12, True)
Bomb_List[73].set(8, 10, True)
Bomb_List[74].set(11, 10, True)
Bomb_List[75].set(9, 16, True)
Bomb_List[76].set(6, 17, True)
Bomb_List[77].set(7, 13, True)
Bomb_List[78].set(18, 11, True)
Bomb_List[79].set(16, 13, True)

Bomb_List[80].set(11, 18, True)
Bomb_List[81].set(11, 14, True)
Bomb_List[82].set(13, 11, True)
Bomb_List[83].set(14, 10, True)
Bomb_List[84].set(2, 17, True)
Bomb_List[85].set(3, 18, True)
Bomb_List[86].set(9, 4, True)
Bomb_List[87].set(4, 16, True)
Bomb_List[88].set(9, 16, True)
Bomb_List[89].set(1, 21, True)

Bomb_List[90].set(17, 2, True)
Bomb_List[91].set(20, 8, True)
Bomb_List[92].set(4, 3, True)
Bomb_List[93].set(9, 8, True)
Bomb_List[94].set(2, 17, True)
Bomb_List[95].set(12, 17, True)
Bomb_List[96].set(13, 16, True)
Bomb_List[97].set(18, 5, True)
Bomb_List[98].set(22, 7, True)
Bomb_List[99].set(7, 18, True)

Bomb_List[100].set(7, 5, True)
Bomb_List[101].set(14, 0, True)
Bomb_List[102].set(13, 1, True)
Bomb_List[103].set(13, 2, True)
Bomb_List[104].set(6, 8, True)
Bomb_List[105].set(10, 13, True)
Bomb_List[106].set(9, 14, True)
Bomb_List[107].set(14, 15, True)
Bomb_List[108].set(15, 14, True)
Bomb_List[109].set(3, 14, True)

Bomb_List[110].set(13, 2, True)
Bomb_List[111].set(13, 9, True)
Bomb_List[112].set(17, 12, True)
Bomb_List[113].set(15, 8, True)
Bomb_List[114].set(6, 8, True)
Bomb_List[115].set(2, 9, True)
Bomb_List[116].set(4, 1, True)
Bomb_List[117].set(14, 3, True)
Bomb_List[118].set(15, 4, True)
Bomb_List[119].set(16, 9, True)

Bomb_List[120].set(12, 14, True)
Bomb_List[121].set(17, 16, True)
Bomb_List[122].set(19, 13, True)
Bomb_List[123].set(8, 12, True)
Bomb_List[124].set(9, 17, True)
Bomb_List[125].set(16, 7, True)
Bomb_List[126].set(10, 2, True)
Bomb_List[127].set(16, 4, True)
Bomb_List[128].set(18, 3, True)
Bomb_List[129].set(21, 6, True)

Bomb_List[130].set(0, 16, True)
Bomb_List[131].set(1, 15, True)
Bomb_List[132].set(19, 13, True)
Bomb_List[133].set(8, 12, True)
Bomb_List[134].set(9, 17, True)
Bomb_List[135].set(16, 7, True)
Bomb_List[136].set(2, 19, True)
Bomb_List[137].set(19, 20, True)
Bomb_List[138].set(11, 21, True)
Bomb_List[139].set(12, 20, True)

Bomb_List[140].set(18, 21, True)
Bomb_List[141].set(18, 22, True)