#Напишите программу NumPy, чтобы найти индексы элементов, равные нулю, в массиве numpy. 
import numpy as np
nums = np.array([1,0,2,0,3,0,4,5,6,7,8])
print("Original array:")
print(nums)
print("Indices of elements equal to zero of the said array:")
result = np.where(nums == 0)[0]
print(result)
