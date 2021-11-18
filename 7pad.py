#Напишите программу NumPy, чтобы добавить границу (заполненную нулями) вокруг существующего массива. 
import numpy as np
a = np.ones(9).reshape(3,3)
print(a)
a= np.pad(a, pad_width=1, mode='constant', constant_values=0)
print(a)
