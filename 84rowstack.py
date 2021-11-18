#Напишите программу NumPy, как добавить дополнительный столбец в массив numpy.
import numpy as np
x = np.array([[10,20,30], [40,50,60]])
print(x)
y = np.array([[100], [200]])
print(y)
c = np.append(x, y, axis=1)
print(c)
y = np.append(y,5)
print(y)
d= np.row_stack([x,y])#po strokam
print(d)
