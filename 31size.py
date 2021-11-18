#Напишите программу NumPy, чтобы найти объем памяти массива NumPy. 
import numpy as np
a = np.arange(1,10)
print(a.size*a.itemsize)