import cv2
import numpy as np

overlay_path = "./hat.png"
hat = cv2.imread(overlay_path, cv2.IMREAD_COLOR)
hat = cv2.resize(hat, (int(hat.shape[1] / 2), int(hat.shape[0] / 2)))

cam = cv2.VideoCapture(0)

while True:
    try:
        new_hat=hat.copy()
        ret, frame = cam.read()
        if frame is None:
            continue

        frame = cv2.resize(
            frame, (int(frame.shape[1] / 3), int(frame.shape[0] / 3))
        )
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_clasifier = cv2.CascadeClassifier(
            "./models/haarcascade_frontalface_default.xml"
        )
        face = face_clasifier.detectMultiScale(
            frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )
        if len(face) != 0:
            x, y, w, h = face[0]
            hat_width = hat.shape[1]
            hat_height = hat.shape[0]

            transparent_img = np.zeros((frame.shape[0],frame.shape[1], 3), dtype=np.uint8)

            # -- START

            start_x = x-int(hat_width/5)+10
            start_y = y-int(hat_height/1.5)

            if start_y < 0:
                new_hat = hat[start_y*(-1):hat_height, 0:hat_width]
                end_y = new_hat.shape[0]
                start_y = 0
            else:
                end_y = start_y+hat_height
            end_x = start_x+hat_width

            # Overlay the PNG onto the background
            result_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            transparent_img[start_y: end_y,start_x: end_x] = new_hat

            frame = np.where(transparent_img==0,frame, transparent_img)

            # -- END

        cv2.imshow("webcam", frame)

        if cv2.waitKey(1) == ord("s"):
            breakpoint()
        if cv2.waitKey(1) == ord("q"):
            print(frame.shape)
            break
    except Exception as err:
        print("error!:", err)
        breakpoint()
        continue

# cam.release()
cv2.destroyAllWindows()
