import numpy as np
import cv2

img = np.zeros((500,500), dtype=np.uint8)
cv2.ellipse(img=img, 
            center=(250, 250), 
            axes=(100,50), 
            angle=0,
            startAngle=0,
            endAngle=180,
            color=(255,2255,255), 
            thickness=1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
