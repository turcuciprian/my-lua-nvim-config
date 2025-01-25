import numpy as np
import cv2

def position_text_in_image_middle(img, text="Default text", fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1):
    image_width= img.shape[1]
    image_height= img.shape[0]

    text_size = cv2.getTextSize(text, fontFace,fontScale, 1)
    text_width = text_size[0][0]
    text_height = text_size[0][1]

    x_text_position = int((image_width/2)-(text_width/2))
    y_text_position =int((image_height/2)-(text_height/2))

    cv2.putText(img=img,text=text, org=(x_text_position, y_text_position),fontFace=fontFace,fontScale=1,color=(255,255,255), lineType=cv2.LINE_8,bottomLeftOrigin=False)
    cv2.imshow("image013", img)
    cv2.waitKey(0)
    cv2.imwrite("edited.png",img)

# load an image
img = cv2.imread("test_image.png", cv2.IMREAD_GRAYSCALE)
#use the method
#img = np.zeros((400,900), dtype=np.uint8)
position_text_in_image_middle(img)
