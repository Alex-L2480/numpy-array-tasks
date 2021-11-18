#Напишите программу NumPy для вычисления гистограммы набора данных
import numpy as np    
import matplotlib.pyplot as plt
plt.hist([1, 2, 1], bins=[0, 1, 2, 3, 5])
plt.show()