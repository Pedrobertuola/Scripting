from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.convert('L') 
crooked = filtered_img.rotate(180)
crooked.save("grey.png", 'png')


#filtered_img.show()
