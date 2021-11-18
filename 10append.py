#Напишите программу NumPy для добавления значений в конец массива. 
import numpy as np
x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x,10)
print("After append values to the end of the array:")
print(x)
print(x[3])


