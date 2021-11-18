#Напишите программу NumPy для создания случайного набора строк из 2D-массива.
import numpy as np
new_array = np.random.randint(5, size=(5,3))
print("Random set of rows from 2D array array:")
print(new_array)