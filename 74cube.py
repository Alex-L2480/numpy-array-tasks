 #Написать Программа NumPy для создания куба функции, который кубирует все элементы массива. 
import numpy as np
def cube(e):
    it = np.nditer([e, None])
    for a, b in it:
        b[...] = a*a*a
    return it.operands[1]
print(cube([1,4,3]))