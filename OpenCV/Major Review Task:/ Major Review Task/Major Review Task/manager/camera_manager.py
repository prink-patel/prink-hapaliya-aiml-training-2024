import threading
import cv2
import time
from cam_object.camera_object import *
from cam_object.detect_object import *
from cam_object.desk_obj import *
import pyautogui
import os
import uuid
import numpy as np


class camera_manager:

    print("hello")

    def __init__(self, dic_roi, sources):
        self.sources = sources
        self.dic_roi = dic_roi
        self.camera_dic = {}
        self.count_frame = 0

    def run(self):
        print("camera_manager")
        for camera_id in self.sources:
            self.camera_dic[camera_id] = {}
            self.camera_dic[camera_id]["get_cap"] = {
                "object": camera_object(
                    camera_id, self.dic_roi[camera_id], self.sources[camera_id]
                ),
                "thread": None,
            }
            print("1")
            self.camera_dic[camera_id]["detect_object"] = {
                "object": detect_object(
                    self.camera_dic[camera_id]["get_cap"]["object"].writer_queue,
                    self.dic_roi[camera_id]
                ),
                "thread": None,
            }
            print("2")
            # self.camera_dic[camera_id]["space_time_count"] = {
            #     "object": Place_Occupancy(
            #         self.camera_dic[camera_id]["detect_object"]["object"].writer_queue,
            #         self.dic_roi[camera_id],
            #     ),
            #     "thread": None,
            # }
            # print("3")

        print("created object")

        for camera_id in self.sources:
            for object_dic in self.camera_dic[camera_id]:
                self.camera_dic[camera_id][object_dic]["thread"] = threading.Thread(
                    target=self.camera_dic[camera_id][object_dic]["object"].run
                )
                self.camera_dic[camera_id][object_dic]["thread"].start()

        print("start thread")

        self.display_all()

    def display_all(self):
        time.sleep(1)
        while True:
            for object in self.camera_dic:

                cv2.namedWindow(object, cv2.WINDOW_AUTOSIZE)

                image = self.camera_dic[object]["detect_object"][
                    "object"
                ].writer_queue.get()
                image = cv2.resize(image, (800, 650))

                # imgname = os.path.join(r'/home/wot-prink/Desktop/hello/OpenCV/ Major Review Task/train_image',f'{str(uuid.uuid1())}.jpg')

                # if self.count_frame==25:
                #     cv2.imwrite(imgname, image)
                #     self.count_frame=0
                # else:
                #     self.count_frame=self.count_frame+1

                cv2.imshow(object, image)
                # imgname = os.path.join(r'/home/wot-prink/Desktop/hello/OpenCV/ Major Review Task/train_image',f'{str(uuid.uuid1())}.jpg')
                # cv2.imwrite(imgname, image)
            cv2.waitKey(1)
