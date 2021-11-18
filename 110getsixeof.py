#Напишите программу NumPy, чтобы получить использование памяти массивами numpy. 
import numpy as np
from sys import getsizeof
x = [0] * 1024
y = np.array(x)
print(getsizeof(y))
