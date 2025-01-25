import numpy as np
from PIL import Image

def luminosity(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    #A = img[:,:,3]
    greyscale_img = 0.299*R + 0.587*G + 0.114*B 
    return greyscale_img.astype(np.uint8)

img = Image.open("./background.png")
img.show()
np_img = np.array(img)
new_image = luminosity(np_img)
pilImage = Image.fromarray(new_image)
pilImage.show()
