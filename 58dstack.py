#Напишите программу NumPy для преобразования (по глубине последовательности (вдоль третьей оси)) двух одномерных массивов в двумерный массив.
import numpy as np
a = np.array([0,20,30])
b = np.array([40,50,60])
c = np.dstack((a, b))
print(c)
print(c.shape)
c = np.squeeze(c)
print(c)