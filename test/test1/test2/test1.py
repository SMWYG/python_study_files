from PIL import Image
from skimage.color import rgb2gray
import numpy as np

i = Image.open('C:\\Users\\dahan\\Downloads\\6.jpg')
j = Image.open('C:\\Users\\dahan\\Downloads\\1.jpg')

a=np.array([[[200,200,250]]])
print(rgb2gray(a))
# size=(32,32)
#
# i.thumbnail(size)
# i_raw = i.load()
#
# i_raw[0,18]=(128,128,128)
# print(i_raw[0,18])
# print(i_raw[15,15])

# print(i.size)



