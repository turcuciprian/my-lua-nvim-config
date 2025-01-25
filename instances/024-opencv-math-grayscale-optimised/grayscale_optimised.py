import numpy as np
from datetime import datetime
import cv2

img = cv2.imread("./background.png")


def luminosity(img):
    r, g, b = cv2.split(img)
    greyscale_img = 0.299 * r + 0.587 * g + 0.114 * b
    return greyscale_img.astype(np.uint8)


def optimised_luminousity(img):
    r, g, b = cv2.split(img.astype(np.uint16))
    # img = img.astype(np.int16)
    greyscale_img = (np.dot(299, r) + np.dot(587, g) + np.dot(114, b)) // 1000
    # greyscale_img = ((np.dot(img[:, :, 0] , 298)) + (np.dot(img[:, :, 1] , 587)) + (np.dot(img[:, :, 2] , 114))) // 1000
    greyscale_img[greyscale_img < 0] = 0

    return greyscale_img.astype(np.uint8)


# cv2.imshow("original",img)
# cv2.waitKey(0)
print("floating point vectorization time:")
start_time = datetime.now()
lum = luminosity(img)
end_time = datetime.now()
print((end_time - start_time).total_seconds(), "sec")
cv2.imshow("luminosity", lum)
cv2.waitKey(0)
cv2.destroyWindow("luminousity")
print("int vectorization time:")
start_time = datetime.now()
opt_lum = optimised_luminousity(img)
end_time = datetime.now()
print((end_time - start_time).total_seconds(), "sec")
cv2.imshow("optimised luminosity", opt_lum)
cv2.waitKey(0)
cv2.destroyWindow("optimised luminousity")
