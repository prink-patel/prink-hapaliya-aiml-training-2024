import json
import cv2
import numpy as np
import queue
import pandas as pd
from ultralytics import YOLO
from Detection.Tracker import *

from ultralytics import YOLO


class camera_object:
    def __init__(self, camera_id, dic_roi, source) -> None:
        self.camera_id = camera_id
        self.dic_roi = dic_roi
        self.source = source
        self.writer_queue = queue.Queue(maxsize=1)

    def imgage(self):
        
        for coord in self.dic_roi.values():
            coord = np.array(coord)
            c = np.array([self.width, self.height])

            final_coord = np.array(coord * c,dtype="int64")
            # print(final_coord,self.width,self.height,coord)

            self.frame = cv2.polylines(
                self.frame,
                [final_coord],
                isClosed=True,
                color=[255, 0, 0],
                thickness=3,
            )

    def run(self):
        print("run camera object")
        
        self.cap = cv2.VideoCapture(self.source)

        
            # model = YOLO("yolov8n.pt")
            # result=model(source=1,show=True,conf=0.4,save=True)
        while True:
            ret, self.frame = self.cap.read()
            if not ret:
                break
            self.height, self.width = self.frame.shape[:2]
            self.imgage()
                
            if self.writer_queue.empty():
                self.writer_queue.put(self.frame)
