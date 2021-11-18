#Напишите программу NumPy для создания массива из 10 целых чисел из генератора.
import numpy as np
iterable = (x for x in range(10))
print(np.fromiter(iterable, np.int))