from PIL import Image
img = Image.open('vFrame_square.PNG')
thresh = 150
fn = lambda x : 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
#r.save('foo.png')
r.show()

# FFMPEG OS
#ffmpeg -i rtsp://admin:admin@172.16.13.85:554/live/sub -f image2 -r 1 /mnt/LocalStorage/upload/img%01d.jpg
