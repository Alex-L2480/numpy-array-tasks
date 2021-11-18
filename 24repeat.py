#Напишите программу NumPy для повторения элементов массива.
import numpy as np
x = np.repeat(3, 4)
print(x)
x = np.array([[1,2],[3,4],[5,6]])
print(x)
print(np.repeat(x, 2))