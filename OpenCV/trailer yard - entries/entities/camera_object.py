import json
import cv2
import numpy as np
import queue
from managers.truck_manager import *
from managers.trailer_manager import *


class camera_object:

    def __init__(self, camera_id, data_rois, paths):
        self.camera_id = camera_id
        self.data_rois = data_rois
        self.paths = paths
        json_path = open(self.paths["json_path"])
        self.json_data = json.load(json_path)
        self.truck_manager = truck_manager(
            self.camera_id, self.json_data
        )
        self.writer_queue = queue.Queue(maxsize=1)

    def coords(self):
        self.coord_dic = {}
        for i in range(len(self.data_rois)):
            # self.coord_list.append(self.data_rois[i]["points"])
            self.coord_dic[self.data_rois[i]["roi"]] = self.data_rois[i]["points"]
            

        

    def imgage(self):
        for coord in self.coord_dic.values():
            coord = np.array(coord, dtype="int64")
            self.img = cv2.polylines(
                self.img,
                [coord],
                isClosed=True,
                color=[255, 0, 0],
                thickness=3,
            )
            

    def run(self):
        print("camera_object")
        self.img_path = self.paths["img_path"]
        self.img = cv2.imread(self.img_path)
        self.coords()
        self.imgage()

        for frame_with_id in range(3000, len(self.json_data["messages"])):
            

            img_copy = self.img.copy()
            
            
            self.truck_manager.dictionary_manage(frame_with_id,self.coord_dic,img_copy)
            
            



            self.trailer_manager = trailer_manager(
                img_copy, self.json_data, frame_with_id
            )
            temp_img = self.trailer_manager.run()
            

            timestamp = self.json_data["messages"][frame_with_id]["ts"]
            
            for i in self.coord_dic.keys():
                cv2.putText(
                    temp_img,
                    i,
                    self.coord_dic[i][0],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    4,
                    (0, 0, 250),
                    10,
                )
            
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
    