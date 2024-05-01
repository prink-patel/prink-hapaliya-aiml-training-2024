import cv2
from DataBase.Database import *
from deepface import DeepFace
import uuid
import os


class FaceDetection:
    def __init__(self):
        self.database = Database()

    # Detect face and draw a rectangle around it
    def detect_face(self, frame):
        faces = DeepFace.extract_faces(frame, enforce_detection=False)
        self.draw_bbox(frame, faces) # draw a rectangle around it
        return frame

    # Draw a rectangle around the face 
    def draw_bbox(self, frame, faces):
        for face in faces:
            x, y, w, h, a1, a2 = face["facial_area"].values()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if not (x == 0 or y == 0):
                database_frame = frame[y : y + h, x : x + w]
                self.save_image(database_frame)
                self.send_to_database()
                
    # Save image in face_image folder
    def save_image(self, database_frame):
        self.img_name = os.path.join(r"face_image", f"{str(uuid.uuid1())}.jpg")
        cv2.imwrite(
            self.img_name,
            database_frame,
        )
        
    # Send data to database
    def send_to_database(self):
                data = {"img_name": self.img_name}
                self.database.enter(data)
