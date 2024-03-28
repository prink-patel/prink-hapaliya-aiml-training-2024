DISPLAY_FLAG=True


user_name = "test"
password = "test@1234"

sources = {
# "camera_1": "/home/wot-prink/Downloads/NitroShare/Cam-6-2.mp4",
"camera_1": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=1&subtype=0",
# "camera_2": f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=2&subtype=0",
"camera_2": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=4&subtype=0",
# "camera_3": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=3&subtype=0",
}

json_link="/home/wot-prink/Desktop/hello/he/Major Review Task/ Major Review Task/Major_Review_Task/roi.json"
model_path="/home/wot-prink/Desktop/hello/he/Major Review Task/ Major Review Task/Major_Review_Task/models/best (5).pt"
