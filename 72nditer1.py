#Напишите программу NumPy для объединения одно- и двухмерного массива вместе и отображения их элементов.
import numpy as np
x = np.arange(4)
print("One dimensional array:")
print(x)
y = np.arange(8).reshape(2,4)
print("Two dimensional array:")
print(y)
for a, b in np.nditer([x,y]):
    print("%d:%d" % (a,b),)