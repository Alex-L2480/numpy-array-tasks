#Напишите программу NumPy для вставки новой оси в двумерный массив.
import numpy as np
x = np.zeros((3, 4))
print(x.shape)
y = np.expand_dims(x, axis=1).shape
print(y)