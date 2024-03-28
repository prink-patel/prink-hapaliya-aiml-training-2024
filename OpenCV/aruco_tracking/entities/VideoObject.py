import cv2
import queue
import numpy as np
from managers.PalletManager import *

class VideoObject:
    def __init__(self, camera_id, url, roi) -> None:
        self.url = url
        self.roi = roi
        self.camera_id = camera_id
        self.writer_queue = queue.Queue(maxsize=1)
        print("Videoobject", camera_id)
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000)
        self.parameters = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.parameters)
        self.count_=0
        self.Pallet_Manager=PalletManager(self.roi,camera_id)
        
        
    def imgage(self):
        for range_ in self.roi:
            coord = range_["points"]
            # for coord in range_.values():
            coord = np.array(coord)
            c = np.array([self.width, self.height])

            final_coord = np.array(coord * c, dtype="int64")
            # print(final_coord,self.width,self.height,coord)
            self.frame = cv2.polylines(
                self.frame,
                [final_coord],
                isClosed=True,
                color=[255, 0, 0],
                thickness=3,
            )

    def detect_object(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = self.detector.detectMarkers(gray)
        
        if ids is not None:
            for corner,id_ in zip(corners,ids):
                
                corner = corner.astype("int64")
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(self.frame,  
                    str(*id_),  
                    corner[0][0],  
                    font, 1,  
                    (0, 255, 255),  
                    2,  
                    cv2.LINE_4) 
                self.frame = cv2.polylines(
                    self.frame, corner, isClosed=True, color=[0, 255, 0], thickness=3
                )
                
                fps = self.cap.get(cv2.CAP_PROP_FPS)
                self.count_=self.count_+1
                durationInSeconds = self.count_ // fps

                
                self.Pallet_Manager.run(id_,corner,self.height,self.width,durationInSeconds)
                

    def run(self):
        self.cap = cv2.VideoCapture(self.url)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        while True:
            self.ret, self.frame = self.cap.read()
            if not self.ret:
                break
            self.height, self.width = self.frame.shape[:2]
            self.imgage()
            self.detect_object()

            if self.writer_queue.empty():
                self.writer_queue.put(self.frame)
