import cv2
from DataBase.Database import *
from deepface import DeepFace
import uuid
import os


class FaceDetection:
    def __init__(self):
        print("facedetection started")
        self.database = Database()

    def detect_face(self, frame):
        print("inside detect face")
        faces = DeepFace.extract_faces(frame, enforce_detection=False)
        self.draw_bbox(frame, faces)
        return frame

    def draw_bbox(self, frame, faces):
        for face in faces:
            print(face["facial_area"].values())
            x, y, w, h, a1, a2 = face["facial_area"].values()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if not (x == 0 or y == 0):
                print("--------------------------------------")
                database_frame = frame[y : y + h, x : x + w]
                img_name = os.path.join(r"face_image", f"{str(uuid.uuid1())}.jpg")
                cv2.imwrite(
                    img_name,
                    database_frame,
                )
                data = {"img_name": img_name}
                self.database.enter(data)

                # self.database.enter("live_stream_data",data)
