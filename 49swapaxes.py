#Напишите программу NumPy для обмена двумя осями массива.
import numpy as np
a = np.array([[1,2,3]])
print(a)
y =  np.swapaxes(a,1,0)
print(y)
