import cv2

cam = cv2.VideoCapture(0)
# cam.release()
# cv2.destroyAllWindows()

while True:
    ret, frame = cam.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (640, 480))
    face_clasifier = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")
    face = face_clasifier.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    try:
        x, y, w, h = face[0]

        startx = x + int(w / 2)
        starty = y
        endx = x + int(w / 2)
        endy = y + h

        startx2 = x
        starty2 = y + int(h / 2)
        endx2 = x + w
        endy2 = starty2

        cv2.line(
            img=frame,
            pt1=(startx, starty),
            pt2=(endx, endy),
            color=(0, 0, 255),
            thickness=2,
        )

        cv2.line(
            img=frame,
            pt1=(startx2, starty2),
            pt2=(endx2, endy2),
            color=(0, 0, 255),
            thickness=2,
        )

        # cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255),2)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("webcam", frame)
        if cv2.waitKey(1) == ord("s"):
            breakpoint()
        if cv2.waitKey(1) == ord("q"):
            print(frame.shape)
            break
    except:
        continue

# cam.release()
cv2.destroyAllWindows()
