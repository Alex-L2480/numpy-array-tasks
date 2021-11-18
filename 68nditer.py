#Напишите программу NumPy для отображения каждого элемента массива.
import numpy as np
x = np.arange(12).reshape(3, 4)
for a in np.nditer(x):
    print(a,end=' ')
print()