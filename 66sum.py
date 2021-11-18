#Напишите программу NumPy (используя numpy) для суммирования всех кратных 3 или 5 ниже 100. 
import numpy as np
x = np.arange(1, 100)
# find  multiple of 3 or 5
n= x[(x % 3 == 0) | (x % 5 == 0)]
print(n)
# print sum the numbers
print(n.sum())
