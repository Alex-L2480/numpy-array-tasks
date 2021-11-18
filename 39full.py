#Напишите программу NumPy для создания нового массива 3 * 5, заполненного 2.
import numpy as np
a = np.repeat(2,15).reshape(3,5)
print(a)
x = np.full((3, 5), 2)
print(x)