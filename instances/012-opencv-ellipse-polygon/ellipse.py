import cv2
import numpy as np

img = np.zeros(( 500,500), dtype=np.uint8)
cv2.ellipse(img, (250,250),(50,50),180, 0, 90,( 255, 255, 255 ), -1)
cv2.imshow("image with ellipse", img)
cv2.waitKey(0)
