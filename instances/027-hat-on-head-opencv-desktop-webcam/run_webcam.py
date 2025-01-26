import cv2
import sys
import os
import numpy as np
from PIL import Image

# support for importing custom library -- START
current_folder = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_folder, "../.."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# support for importing custom library -- END

overlay_path = os.path.join(current_folder, "hat.png")
hat = Image.open(overlay_path).convert("RGBA")
hat = hat.resize((int(hat.size[0] / 2), int(hat.size[1] / 2)))

cam = cv2.VideoCapture(0)

while True:
    try:
        ret, frame = cam.read()
        if frame is None:
            continue

        new_frame = cv2.resize(
            frame, (int(frame.shape[1] / 3), int(frame.shape[0] / 3))
        )
        new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2RGB)

        face_clasifier = cv2.CascadeClassifier(
            os.path.join(current_folder, "models/haarcascade_frontalface_default.xml")
        )
        face = face_clasifier.detectMultiScale(
            new_frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )

        x, y, w, h = face[0]
        hat_width = hat.size[0]
        hat_height = hat.size[1]
        # -- START

        background_pil = Image.fromarray(new_frame)
        position = (x - 20, y - int(h / 2))
        # Overlay the PNG onto the background
        background_pil.paste(hat, position, mask=hat)
        result = np.array(background_pil)
        result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
        cv2.imshow("Result", result_bgr)

        # -- END

        # cv2.imshow("webcam", new_frame)
        if cv2.waitKey(1) == ord("s"):
            breakpoint()
        if cv2.waitKey(1) == ord("q"):
            print(new_frame.shape)
            break
    except Exception as err:
        print("error!:", err)
        continue

# cam.release()
cv2.destroyAllWindows()
