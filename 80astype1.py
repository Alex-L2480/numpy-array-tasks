#Напишите программу NumPy для преобразования массива чисел с плавающей точкой в массив целых чисел.
import numpy as np
a = np.array([1,2],dtype=float)
print(a)
a = a.astype(int)
print(a)