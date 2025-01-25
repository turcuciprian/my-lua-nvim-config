import cv2

img = cv2.imread("desktop2.png")
img_width = img.shape[1]
img_height = img.shape[0]
percentage = 0.2
img = cv2.resize(img, (int(img_width*percentage), int(img_height*percentage)))
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
