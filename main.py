import PIL
from PIL import Image, ImageEnhance

#Muhammad Yusuf (011180142)

#folder
gambar ="img/tes1.png"

#read the image
im = Image.open(gambar)

#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)

factor = 1 ##Akan menghasilkan original
im_output = enhancer.enhance(factor)
im_output.save('gambar-original.png')

factor = 0.25 #Akan menghasilkan gelap
im_output = enhancer.enhance(factor)
im_output.save('gambar-gelap.png')

factor = 1.5 #Akan menghasilkan terang
im_output = enhancer.enhance(factor)
im_output.save('gambar-terang.png')
