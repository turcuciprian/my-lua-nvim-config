import numpy as np
import cv2

background = cv2.imread("./background.png")
overlay = cv2.imread("./overlay.png")
transparent_img = np.zeros((background.shape[0],background.shape[1], 3), dtype=np.uint8)
transparent_img[20:20+overlay.shape[0],100:100+overlay.shape[1]] = overlay
result = cv2.addWeighted(background, 1, transparent_img, 0.5, 0)
cv2.imshow("image overlayed", result)
cv2.waitKey(0)
