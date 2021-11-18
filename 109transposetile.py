#Напишите программу NumPy для создания декартового произведения двух массивов в один массив двумерных точек.
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5])
result = np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
print(result)

a = np.array([1, 2])
b = np.tile(a, 2)
print(b)