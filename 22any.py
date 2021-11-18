#Напишите программу NumPy, чтобы проверить, имеет ли какой-либо элемент массива вдоль заданной оси значение True.
import numpy as np
print(np.any([[False,False],[False,False]]))
print(np.any([[True,True],[True,True]]))
print(np.any([10, 20, 0, -50]))#0-true
print(np.any([10, 20, -50]))
