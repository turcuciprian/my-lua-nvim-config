import numpy as np
import cv2


img = cv2.imread("test_image.png", cv2.IMREAD_UNCHANGED)
crop_width = img.shape[1]
crop_height = 50
img_height = int( img[0].shape[0] )
img_width = int( img[1].shape[0] )
start_y = int( img_height/2- crop_height/2)
end_y = int( img_height/2+crop_height/2 )
start_x = int( img_width/2-crop_width/2 )
end_x = int( img_width/2+crop_width/2 )
crop = img[start_y:end_y,start_x:end_x]
img[0][0:] = [ 0,  0,  255, 255]
cv2.imshow("image", img)
cv2.imshow("crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
