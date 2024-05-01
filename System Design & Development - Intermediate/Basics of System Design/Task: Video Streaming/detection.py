from flask import Flask
from LogindataManager.GetLoginData import *
import cv2
import base64
import numpy as np
from Detection.FaceDetection import *
from flask_socketio import SocketIO
from flask_socketio import emit


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

face_detection = FaceDetection()

@socketio.on("send_frame")
def detect(data):
    image = data["frame"]
    image = base64.b64decode(image.split(",")[1])
    image = np.frombuffer(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    detect_frame = face_detection.detect_face(image)
    send_detect_frame = base64.b64encode(cv2.imencode(".jpg", detect_frame)[1]).decode()
    emit("send_frame_js", {"frame": send_detect_frame})


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)
