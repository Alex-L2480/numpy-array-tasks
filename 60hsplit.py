#Напишите программу NumPy, чтобы разбить массив формы 4x4 на два массива вдоль второй оси.
import numpy as np
x = np.arange(16).reshape((4, 4))
print("Original array:",x)
print("After splitting horizontally:")
print(np.hsplit(x, [2]))