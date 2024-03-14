from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict('rtsp://test:test@1234@192.168.44.245:554/cam/realmonitor?channel=2&subtype=0', imgsz=920, show=True, conf=0.4, save=True)
