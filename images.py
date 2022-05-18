from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR) #BLUR/SMOOTH/SHARPEN
filtered_img = img.convert('L') #img become black and white
filtered_img.save("grey.png", 'png')
#print(img.size)  #img.size