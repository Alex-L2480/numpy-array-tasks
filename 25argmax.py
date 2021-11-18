#Напишите программу NumPy, чтобы найти индексы максимальных и минимальных значений вдоль заданной оси массива. 
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("Original array: ",x)
print("Maximum Values: ",np.argmax(x))
print("Minimum Values: ",np.argmin(x))
print(x[5])