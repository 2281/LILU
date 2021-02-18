import numpy as np
from PIL import Image

vFrame = Image.open('vFrame_square.png')
gray_vFrame = vFrame.convert('1')

width, height = gray_vFrame.size
new_height = 256
new_width = int(new_height * width / height)

#РЕСАЙЗ
gray_vFrame = gray_vFrame.resize((new_width, new_height), Image.ANTIALIAS)

#ПОКАЗ
gray_vFrame.show()

#ВЗЯТЬ ПИКСЕЛИ ИЗОБРАЖЕНИЯ В МАССИВ
gray_pixels = list(gray_vFrame.getdata())


#В МАССИВ NUMPY
gray_arr = np.array(gray_vFrame) # 640x480x4 array
print(gray_arr)
#gray_arr = gray_arr[16, 16] # 4-vector, just like abovei

# FFMPEG OS
#ffmpeg -i rtsp://admin:admin1337@172.16.13.85:554/live/sub -f image2 -r 1 /mnt/LocalStorage/upload/img%01d.jpg
