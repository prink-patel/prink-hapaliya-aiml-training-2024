import os
import cv2
import numpy as np
import queue
from managers.trailer_manager import *


class camera_object:

    def __init__(self, data_rois, paths):
        self.data_rois = data_rois
        self.paths = paths
        self.writer_queue = queue.Queue(maxsize=1)

    def coords(self):
        self.coord_list = []
        for i in range(len(self.data_rois)):
            self.coord_list.append(self.data_rois[i]["points"])

    def imgage(self):
        for coord in self.coord_list:
            coord = np.array(coord, dtype="int64")
            self.img = cv2.polylines(
                self.img,
                [coord],
                isClosed=True,
                color=[255, 0, 0],
                thickness=3,
            )

    def run(self):

        self.img_path = self.paths["img_path"]
        self.img = cv2.imread(self.img_path)
        self.coords()
        self.imgage()
        json_path = open(self.paths["json_path"])
        data = json.load(json_path)

        for frame_id in range(len(data["messages"])):
            img_copy = self.img.copy()
            
            # trailer manager
            self.trailer_manager = trailer_manager(img_copy, data, frame_id)
            temp_img = self.trailer_manager.run()

            timestamp = data["messages"][frame_id]["ts"]
            cv2.putText(
                temp_img,
                "Timestamp: " + str(timestamp),
                (100, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (0, 0, 250),
                10,
            )
            if self.writer_queue.empty():
                self.writer_queue.put(temp_img)
