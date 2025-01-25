import numpy as np
import cv2

img = cv2.imread("./background.png")
#breakpoint()
def lightness(img):
    r,g,b = cv2.split(img)
    min_result= np.minimum(np.minimum(r,g),b)
    max_result = np.maximum(np.maximum(r,g),b) 
    greyscale_img = (min_result  + max_result)  / 2
    return greyscale_img.astype(np.uint8)

def average(img):
    r,g,b = cv2.split(img)
    greyscale_img = ( r+g+b )
    return greyscale_img.astype(np.uint8)

def luminosity(img):
    r,g,b = cv2.split(img)
    cv2.imshow("red", r.astype(np.uint8))
    cv2.waitKey(0)
    greyscale_img = 0.299*r + 0.587*g + 0.114*b
    return greyscale_img.astype(np.uint8)

cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyWindow("original")
cv2.imshow("lightness",lightness(img))
cv2.waitKey(0)
cv2.destroyWindow("lightness")
cv2.imshow("average",average(img))
cv2.waitKey(0)
cv2.destroyWindow("average")
cv2.imshow("luminosity",luminosity(img))
cv2.waitKey(0)
cv2.destroyWindow("luminousity")
