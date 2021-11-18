#Напишите программу NumPy для сортировки пар имени и фамилии, возвращающих их индексы.
import numpy as np
first_names =    ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
x = np.lexsort((first_names, last_names))
print(x)
