#Напишите программу NumPy для создания 2d-массива с 1 на границе и 0 внутри. 
import numpy as np
a = np.ones(25).reshape(5,5)
print(a)
a[1:-1,1:-1] = 0
print(a)
a[:,-1]=2
print(a)