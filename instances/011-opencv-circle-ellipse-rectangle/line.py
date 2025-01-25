import numpy as np
import cv2

img = np.zeros((500,500), dtype=np.uint8)
cv2.line(img=img, 
              pt1=(200, 250), 
              pt2=(300, 275), 
              color=(255,255,255), 
              thickness=1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
