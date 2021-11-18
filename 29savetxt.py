#Напишите программу NumPy для сохранения массива NumPy в текстовый файл
import numpy as np
a = np.arange(1,10)
print(a)
print(a.dtype)
np.savetxt('file.out', a)
b = np.loadtxt('file.out')
print(b)
print(b.dtype)
