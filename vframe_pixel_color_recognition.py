import os
import json
import time
from PIL import Image
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

#r = sr.Recognizer()
#m = sr.Microphone()
mixer.init()

def listen():
    with m as source:
        audio = r.listen(source)
    try:
        statement = r.recognize_google(audio, language="ru_RU")
        print(str(statement))
        # if statement == "null": statement = ""
        return str(statement)
    except KeyboardInterrupt:
        pass

def speek(text):
    #time.sleep(5)
    tts = gTTS(text=text, lang='ru')
    tts.save("speek.mp3")
    mixer.music.load("speek.mp3")
    mixer.music.play()
    #time.sleep(5)

#Simple scheme test
def recognize_color(coefficients):
    R,G,B = coefficients[0],coefficients[1], coefficients[2]
    if R > G and R > B: return ("Красный")
    if G > R and G > B: return ("Зелёный")
    if B > R and B > G: return ("Синий")


#img = Image.open('pixel_blue.png')

#color_code = img.load()
#img.show()

R = 254
G = 255
B = 1

colors = ["red","green","blue"]
coefficients = []

img = Image.new('RGB', (250, 250), (R, G, B))
img.getpixel((0, 0))

#img.putpixel((0, 0), (R, G, B)) # Изменяем цвет пикселя
#(0/255)+(0/255)+(255/255)
#print("Color coefficient 1 = ",1 / (R/255)+(G/255)+(B/255))
#print("Color coefficient 2 = ",(R/255)+(G/255)+(B/255))

if R == 0: print("Red = 0")
else: print("Red = ",(R/255))
coefficients.append(R/255)
if G == 0: print("Green = 0")
else: print("Green = ",(G/255))
coefficients.append(G/255)
if B == 0: print("Blue = 0")
else: print("Blue = ",(B/255))
coefficients.append(B/255)
#print(coefficients)

img.show()
recognized_color = recognize_color(coefficients)
print(recognized_color)
speek(recognized_color)

time.sleep(2)


#print(dict(zip(colors, coefficients)))

#20 20 20 Color coefficient =  0.23529411764705882


#img.getpixel((0, 0))              # Получаем цвет пикселя
#(255, 0, 0)
#img.show()                          # Просматриваем изображение

#img.save("pixel_blue_1.jpg")          # В формате JPEG
#img.save("pixel_blue_1.bmp", "BMP")   # В формате BMP
#img.save("pixel_blue_1.png", "PNG")
#f = open("pixel_blue_1.jpg", "wb")
#img.save(f, "PNG")           # Передаем файловый объект
#.close()