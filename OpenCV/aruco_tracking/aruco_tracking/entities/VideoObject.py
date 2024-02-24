import cv2
import numpy as np
from shapely.geometry import Point, LineString, Polygon

import sys

# from aruco_tracking.managers.PalletManager import PalletManager

sys.path.insert(1,"/home/wot-prink/Downloads/aruco_tracking-20240223T114103Z-001/aruco_tracking/managers")
from PalletManager import *


class VideoObject:

    def __init__(self, data):
        self.data = data
        self.url = data["url"]
        self.roi_points = data["rois"]
        self.roi_1 = self.roi_points[0]["points"]
        self.roi_2 = self.roi_points[1]["points"]
        self.cap = cv2.VideoCapture(self.url)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.count=None
        
    def detect(self):
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000)
        self.parameters = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.parameters)
        while True:
            self.ret, self.frame = self.cap.read()
            if self.ret:
                self.height, self.width = self.frame.shape[:2]
                self.roi11 = (self.roi_1 * np.array([self.width, self.height])).astype(
                    "int64"
                )
                self.roi22 = (self.roi_2 * np.array([self.width, self.height])).astype(
                    "int64"
                )

                self.roi1 = Polygon(self.roi11)
                self.roi2 = Polygon(self.roi22)
                self.coords1 = np.array([[*self.roi1.exterior.coords]]).astype("int64")
                self.coords2 = np.array([[*self.roi2.exterior.coords]]).astype("int64")

                self.frame = cv2.polylines(self.frame,self.coords1,isClosed=True,color=[255, 0, 0],thickness=3)
                self.frame = cv2.polylines(self.frame,self.coords2,isClosed=True,color=[255, 0, 0],thickness=3)

                self.palletmanager = PalletManager(self.roi1,self.roi2)

                self.frame,self.count = self.palletmanager.run(self.frame,self.count)

                self.frame = cv2.resize(self.frame, (900, 600))
                cv2.imshow(self.url, self.frame)
                keyCode = cv2.waitKey(int(1000 / self.fps))
                if keyCode & 0xFF == ord("q"):
                    break
        cv2.destroyAllWindows()
