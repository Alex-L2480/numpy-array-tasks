#Напишите программу NumPy для перемещения осей массива на новые позиции.
import numpy as np
x = np.array([[[1,2],[3,4],[5,6]]])
print(x)
print(np.moveaxis(x, 0, -1).shape)
print(x)
print(np.moveaxis(x, -1, 0).shape)
print(x)