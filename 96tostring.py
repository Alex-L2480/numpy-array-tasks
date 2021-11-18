#Напишите программу NumPy для преобразования необработанных данных в массиве в двоичную строку, а затем создайте массив.
import numpy as np
x = np.array([10, 20, 30], float)
print("Original array:")
print(x)
s = x.tostring()
print("Binary string array:")
print(s)
print("Array using fromstring():")
y = np.fromstring(s)
print(y)

