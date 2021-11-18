#Напишите программу NumPy для преобразования изображения PIL в массив numpy
import numpy as np
import PIL
from PIL import Image
img_data = Image.open('balloon_PNG4969_yapfiles.ru.png' )
img_arr = np.array(img_data) 
print(img_arr)
