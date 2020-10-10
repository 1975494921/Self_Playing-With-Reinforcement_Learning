

def print_table(table,ACTIONS,x_size,y_size,trea_x,trea_y):
    print('                 left    right    up    down')
    for x in range(x_size):
        for y in range(y_size):
            if not ((x == trea_x) and (y == trea_y)):
                print('(', x, ',', y, '):    ', end='')
                for act in range(len(ACTIONS)):
                    print(table[x, y, act], '     ', end='')
                print('')