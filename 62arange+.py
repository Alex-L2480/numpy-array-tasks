#Напишите программу NumPy для создания матрицы 5x5 со значениями строк в диапазоне от 0 до 4.
import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("Row values ranging from 0 to 4.")
x += np.arange(5)
print(x)