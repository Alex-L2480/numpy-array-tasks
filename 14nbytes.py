#Напишите программу NumPy, чтобы найти количество элементов массива, длину одного элемента массива в байтах и общее количество байтов, потребляемых элементами.
import numpy as np
a = np.arange(1,10).reshape(3,3)
print(a)
print(a.size)
print(a.itemsize)
print(a.size*a.itemsize)
print(a.nbytes)