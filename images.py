from PIL import Image , ImageFilter 
img = Image.open('./py/pikachu.jpg')
print(img)
# image formatting
print(img.format)
#size
print(img.size)
# mode 
print(img.mode)
#directory 
print(dir(img))
#filtering
filtered_img=img.filter(ImageFilter.BLUR)
print(img)
#to save it 
filtered_img.save("blur.png",'png')
#smooth filter
filtered_img.save("smooth.png",'png')
#sharpen 
filtered_img.save("sharpen.png",'png')
#we can convert 
filtered_image = img.convert('L')
crucked = filtered_img.rotate(90)
crucked .save("grey.png",'png')
#to show 
filtered_img.show()
#to rotate
crucked = filtered_img.rotate(90)
#to resize
resize = filtered_image.resize((300,300))
#to crop
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save("grey.png",'png')

 