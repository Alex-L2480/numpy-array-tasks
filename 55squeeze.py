#Напишите программу NumPy для удаления одномерных записей из заданной фигуры.
import numpy as np
x = np.zeros((3, 1, 4))
print(np.squeeze(x).shape)

