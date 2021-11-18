#Напишите программу NumPy для создания массива из 10 с одинаковой формой и типом данного массива.
import numpy as np
x = np.arange(4, dtype=np.int64)
print(x)
y = np.full_like(x, 10)
print(y)

