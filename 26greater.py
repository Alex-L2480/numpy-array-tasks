#Напишите программу NumPy для сравнения двух массивов, используя numpy. 
import numpy as np
a = np.array([1, 2])
b = np.array([4, 5])
print("Array a: ",a)
print("Array b: ",b)
print("a > b")
print(np.greater(a, b))
print("a >= b")
print(np.greater_equal(a, b))
print("a < b")
print(np.less(a, b))
print("a <= b")
print(np.less_equal(a, b))