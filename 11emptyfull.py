#Напишите программу NumPy для создания пустого и полного массива. 
import numpy as np
# Create an empty array
x = np.empty((3,4))
print(x)
# Create a full array
y = np.full((3,3),np.random.randint(1,10))
print(y)
