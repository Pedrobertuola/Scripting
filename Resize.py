from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
#new_img = img.resize((400, 400))
img.thumbnail((400, 400)) # keep the aspect ratio
img.save('thumbnail.jpg')

print(img.size)