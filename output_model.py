from table_show import print_table
import os
import numpy as np

model_path = 'Model.npy'
if os.path.exists(model_path):
    table = np.load(model_path)
    print_table(table)
else:
    print('Model NOT EXISTED')