import numpy as np#Напишите программу NumPy для преобразования списка и кортежа в массивы.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
b = np.asarray(my_list)
print(b)
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
c = np.asarray(my_tuple)
print(c)