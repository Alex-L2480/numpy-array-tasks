#Напишите программу NumPy для просмотра входных данных в виде массивов как минимум с двумя измерениями, тремя измерениями.
import numpy as np
x = 10
print("View inputs as arrays with at least two dimensions:")
print(np.atleast_1d(x))
x = np.arange(4.0).reshape(2, 2)
print(np.atleast_1d(x))
print("View inputs as arrays with at least three dimensions:")
x =15
print(np.atleast_3d(x))
x = np.arange(3.0)
print(np.atleast_3d(x))
