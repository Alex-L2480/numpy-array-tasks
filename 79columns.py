#Напишите программу NumPy для доступа к массиву по столбцам.
import numpy as np
x= np.arange(9).reshape(3,3)
print("Original array elements:")
print(x)
print("Access an array by column:")
print("First column:")
print(x[:,0])
print("Second column:")
print(x[:,1])
print("Third column:")
print(x[:,2])
