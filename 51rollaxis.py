#Напишите программу NumPy для перемещения указанной оси назад, пока она не окажется в заданной позиции. 
import numpy as np
x = np.ones((2,3,4,5))
print(np.rollaxis(x, 3, 2).shape)
