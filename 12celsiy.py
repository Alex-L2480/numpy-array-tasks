#Напишите программу NumPy для преобразования значений градусов Цельсия в градусы Фаренгейта. Значения Цельсия сохраняются в массиве NumPy
import numpy as np
fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
a = 5*F/9 - 5*32/9
print(a.round())