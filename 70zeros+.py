# Напишите программу NumPy для создания куба размером 5x5x5 из 1.
import numpy as np
a = np.ones((5,5,5))
print(a)

x = np.zeros((5, 5, 5)).astype(int) + 3
print(x)