#processing with a high 3.8mb image 
from PIL import Image ,ImageFilter

astro = Image.open('./astro.jpg')
printing the size
print(astro.size)
# to resize 
new_img.save('thumbnail.jpg')
# to make it look perfect 
astro.thumbnail((400,200))
astro.save('thumbanil.jpg')
print(astro.size)