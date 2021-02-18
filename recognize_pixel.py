import numpy as np
from PIL import Image

#img = Image.open('test-9pixels-green-black.png')
vFrame = Image.open('vFrame_square.png')

arr = np.array(vFrame) # 640x480x4 array
arr[20, 30] # 4-vector, just like abovei

arr = np.array(vFrame) # 640x480x4 array
arr[20, 30] # 4-vector, just like abovei

print('*'*8)
print(arr)

#ЦВЕТНОЙ ВИДЕОФРЕЙМ
#pixels = list(vFrame.getdata())
#print(len(pixels))
#print(pixels)


#ОБЕСЦВЕЧЕННЫЙ ВИДЕОФРЕЙМ
gray_vFrame = vFrame.convert('L')

#gray_pixels = list(gray_vFrame.getdata())
#print(len(gray_pixels))
#print(set(gray_pixels))
#print(len(set(gray_pixels)))

#grayscale.show()

gray_arr = np.array(gray_vFrame) # 640x480x4 array
gray_arr[20, 30] # 4-vector, just like abovei
print('*'*8)
print(gray_arr)