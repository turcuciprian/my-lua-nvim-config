import cv2

def detect_objects(image, objects, lines:bool = False, rectangles:bool = True, window_name:str = "Webcam"):
        for obj in objects:
            try:
                x, y, w, h = obj

                if lines is True:
                    startx = x + int(w / 2)
                    starty = y
                    endx = x + int(w / 2)
                    endy = y + h

                    startx2 = x
                    starty2 = y + int(h / 2)
                    endx2 = x + w
                    endy2 = starty2

                    cv2.line(
                        img=image,
                        pt1=(startx, starty),
                        pt2=(endx, endy),
                        color=(0, 0, 255),
                        thickness=2,
                    )

                    cv2.line(
                        img=image,
                        pt1=(startx2, starty2),
                        pt2=(endx2, endy2),
                        color=(0, 0, 255),
                        thickness=2,
                    )

                if rectangles is True:
                    cv2.rectangle(image, (x,y),(x+w, y+h), (0,0,255),2)
                cv2.imshow(window_name, image)
            except Exception as error:
                print('error', error)
