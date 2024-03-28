import json
import cv2
import numpy as np
import queue
import pandas as pd
from ultralytics import YOLO
import logging
logger = logging.getLogger("smart_system")

class CameraObject:
    def __init__(self, camera_id, desk_roi, source) -> None:
        logger.info(f"call {__name__}")
        self.camera_id = camera_id
        self.desk_roi = desk_roi
        self.source = source
        self.writer_queue = queue.Queue(maxsize=1)

    # normalize roi to denormalize roi convert and draw polyline in frame
    def imgage(self):
        for coord in self.desk_roi.values():
            
            coord = np.array(coord)
            mux_value = np.array([self.width, self.height])
            final_coord = np.array(coord * mux_value,dtype="int64")
            self.frame = cv2.polylines(
                self.frame,
                [final_coord],
                isClosed=True,
                color=[255, 0, 0],
                thickness=3,
            )

    def run(self):
        logger.info(f"{self.camera_id} : run {__name__}")
        self.cap = cv2.VideoCapture(self.source)
        while self.cap:
            ret, self.frame = self.cap.read()
            if not ret:
                logger.critical(f"video not read ret is empty")
                break
            else:
                self.height, self.width = self.frame.shape[:2]
                self.imgage()
                    
                if self.writer_queue.empty():
                    self.writer_queue.put(self.frame)
