from PIL import Image,ImageFilter

img=Image.open("pikachu.png")
filter_img=img.filter(ImageFilter.BLUR)
filter_img.save("blur.png",'png')