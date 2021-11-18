#Напишите программу NumPy для чтения файла данных CSV и сохранения записей в массиве.
from numpy import genfromtxt
csv_data = genfromtxt("test.csv", delimiter=",")
print(csv_data)