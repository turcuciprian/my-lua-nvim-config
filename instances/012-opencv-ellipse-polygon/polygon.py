import cv2
import numpy as np
img = np.zeros(( 500,500), dtype=np.uint8)
pts = np.array([
    [210,305],
    [290,300],
    [270,310],
    [250,340],
    [280,340]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(img, [pts], (255,255,255),1)
cv2.imshow("image with ellipse", img)
cv2.waitKey(0)
