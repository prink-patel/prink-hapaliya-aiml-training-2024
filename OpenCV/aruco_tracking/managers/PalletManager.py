import sys
import cv2
from shapely.geometry import Point, LineString, Polygon
import datetime

# sys.path.insert(1,"/home/wot-prink/Downloads/aruco_tracking-20240223T114103Z-001/aruco_tracking/entities")
# from PalletObject import *


class PalletManager:

    def __init__(self, roi1, roi2):
        self.roi_1 = roi1
        self.roi_2 = roi2
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000)
        self.parameters = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.parameters)
        self.checks = {}

    def run(self, frame, count):

        self.frame = frame
        self.count = count
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = self.detector.detectMarkers(gray)

        for corner in corners:

            corner = corner.astype("int64")
            # print(corner)
            if ids is not None:
                for id in ids:
                    # print(id)
                    # if id not in checks.keys():
                    #     checks[str(*id)] = False
                    string_id = str(*id)
                    c = Polygon(*corner)
                    if not self.roi_1.intersection(c).is_empty:
                        if count == None:
                            count = 1
                        if string_id not in self.checks.keys() and count == 1:
                            # print("video_id ", string_id)

                            print("out")
                            self.checks[string_id] = 1
                            print("check", self.checks)
                            count = 0
                    elif not self.roi_2.intersection(c).is_empty:
                        if count == None:
                            count = 0
                        if string_id not in self.checks.keys() and count == 0:
                            # print("video_id ", string_id)

                            print("in")
                            self.checks[string_id] = 0
                            print("check", self.checks)
                            count = 1
                    else:
                        pass

                    # for key,status in self.checks.items():

                    #     self.palletobject = PalletObject(self.key,status)

                    #     self.palletobject.object()()

                    # print(self.checks,"       ",count)
            self.frame = cv2.polylines(
                self.frame, corner, isClosed=True, color=[0, 255, 0], thickness=3
            )

        return self.frame, count
