import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow("webcam", frame)
    cv2.waitKey(0)
    if cv2.waitKey(1) == 'q':
        break

cv2.destroyAllWindows()
