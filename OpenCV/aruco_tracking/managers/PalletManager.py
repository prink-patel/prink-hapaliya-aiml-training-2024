import cv2
from entities.PalletObject import *
from shapely.geometry import Point, LineString, Polygon
import numpy as np


class PalletManager:
    def __init__(self, roi,camera_id) -> None:
        self.roi = roi
        self.camera_id=camera_id
        self.pallet_dic = {}

    def run(self, id_, corner, height, width,durationInSeconds):
        self.id = int(id_)
        self.corner = corner
        self.height = height
        self.width = width
        self.durationInSeconds=durationInSeconds
        c = Polygon(*corner)
        if self.id not in self.pallet_dic.keys():
            self.pallet_dic[self.id] = PalletObject(self.id,self.camera_id)
        for roi in self.roi:
            coord = np.array(roi["points"])
            mul = np.array([self.width, self.height])
            final_coord = np.array(coord * mul, dtype="int64")
            roi_ = Polygon(final_coord)
            # print("----",roi_.intersection(c).area)
            
            if roi_.intersection(c):
                # print("------------")
                # print(roi["roi_name"])
                self.pallet_dic[self.id].status_(roi["roi_name"],self.durationInSeconds)
