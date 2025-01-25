from ultralytics import YOLO
model  = YOLO("yolov8l.pt")
results = model("images/test7.jpg", conf = 0.25)
for result in results:
    result.show()
    #result.save("images/output/test.jpg")
    #breakpoint()
