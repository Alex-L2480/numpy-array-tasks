#Напишите программу NumPy, чтобы сделать массив неизменным (только для чтения).
import numpy as np
x = np.zeros(10)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1
