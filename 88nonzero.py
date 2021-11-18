#Напишите программу NumPy для удаления отрицательных значений в массиве NumPy с 0. 
import numpy as np
x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print("Original array:")
print(x)
print("Replace the negative values of the said array with 0:")
x[x < 0] = 0
print(x)
x = np.nonzero(x)
x=x[0]
print(x)
print(x[0])