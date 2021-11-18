#Напишите программу NumPy, чтобы получить величину вектора в numpy.
import numpy as np
x = np.array([1,2,3,4,5])
print("Original array:")
print(x)
print("Magnitude of the vector:")
print(np.linalg.norm(x))