#Напишите программу NumPy для преобразования одномерных массивов в виде столбцов в двумерный массив.
import numpy as np
a = np.array((10,20,30))
b = np.array((40,50,60))
c = np.column_stack((a, b))
print(c)