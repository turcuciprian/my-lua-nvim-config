from ultralytics import YOLO
import cv2

def slap_a_label(
    img,
    x,
    y,
    text,
    color=(255, 255, 0),
    fontScale=1,
    thickness=2,
    font=cv2.FONT_HERSHEY_COMPLEX,
):
    point = (x, y-10)
    img = cv2.putText(
        img=img,
        text=text,
        org=point,
        fontFace=font,
        fontScale=fontScale,
        color=color,
        thickness=thickness,
    )
    return img


model = YOLO("yolov8n.pt")

x, y, w, h = (0, 0, 0, 0)

cam = cv2.VideoCapture("./videos/dash_cam.mp4")

while True:
    ret, frame = cam.read()

    # YOLO

    # processing the frame with YOLO
    results = model(frame)
    # looping trough results
    for result in results:
        for box in result.boxes:
            x, y, w, h = tuple(box.xywh[0])

            class_label = result.names[int(box.cls)]
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)

            # calculate top left point positions for x and y
            x_tl = int(x - (w / 2))
            y_tl = int(y - (h / 2))

            # initialise start and end point
            start_point = (x_tl, y_tl)
            end_point = (x_tl + w, y_tl + h)
            # draw the rectangle over the points
            cv2.rectangle(
                frame, pt1=start_point, pt2=end_point, color=(255, 0, 0), thickness=5
            )
            frame = slap_a_label(frame, x_tl, y_tl, class_label)
            # show the frame with the rectangles
            cv2.imshow("main webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
