import numpy as np
import cv2

def change_brightness(image):
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.0
    beta = 50
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
    return new_image
img = cv2.imread("./background.png")
cv2.imshow("copy paste code", change_brightness(img))
cv2.waitKey(0)
contrast = 1.0
brightness  = 50
new_img = np.clip(contrast*img+brightness,0,255)
int_new_img = new_img.astype(int)
cv2.imshow("new_img", int_new_img.astype(np.uint8))
cv2.waitKey(0)

