# Напишите программу NumPy, чтобы разбить массив из 14 элементов на 3 массива, каждый из которых имеет 2, 4 и 8 элементов в исходном порядке
import numpy as np
x = np.arange(1, 15)
print("Original array:",x)
print("After splitting:")
print(np.split(x, [2, 6]))#3 chasti
print(np.split(x, [5]))#2 chasti