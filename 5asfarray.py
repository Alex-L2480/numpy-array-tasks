#Напишите программу NumPy в массив, преобразованный в тип с плавающей точкой.
import numpy as np
a = np.arange(12,38)
print(a)
print(a.dtype)
a = np.asfarray(a)
print(a)
print(a.dtype)
b = a.astype(int)
print(b)
print(b.dtype)

