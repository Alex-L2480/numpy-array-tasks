#Напишите программу NumPy для создания массива (3, 4) формы и преобразования элементов массива в меньшие куски. 
import numpy as np
x= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
print("Above array in small chuncks:")
for a in np.nditer(x, flags=['external_loop'], order='F'):
    print(a)