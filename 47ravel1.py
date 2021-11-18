#Напишите программу NumPy, чтобы свернуть трехмерный массив в один размерный массив.
import numpy as np
a = np.eye(5)
print(a)
a = a.ravel()
print(a)