from PIL import Image
import os


img = Image.open("C:/Users/해피마미/Documents/카카오톡 받은 파일/b.png")

img_resize = img.resize((128, 128))
img_resize.save('생각하는 로댕.png')
print(img_resize.size)