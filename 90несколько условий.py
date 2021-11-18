#Напишите программу NumPy для выбора индексов, удовлетворяющих нескольким условиям в массиве numpy
import numpy as np
a = np.array([97, 101, 105, 111, 117])
b = np.array([0,1,2,3,4])
print("Original arrays")
print(a)
print(b)
print("Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:")
print(b[(100 < a) & (a < 110)])


