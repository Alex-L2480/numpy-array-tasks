#Напишите программу NumPy, чтобы проверить, все ли элементы массива имеют значение True.
import numpy as np
print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50]))#0-false
print(np.all([10, 20, -50]))