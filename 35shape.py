#Напишите программу NumPy для создания двумерного массива размером 2 x 3
import numpy as np
a = np.arange(1,7,dtype = np.int32).reshape(2,3)
print(a)
print(a.dtype)
print(a.shape)

