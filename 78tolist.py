#Напишите программу NumPy для преобразования массива NumPy в структуру списка Python
import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
b = x.tolist()
print(b)
