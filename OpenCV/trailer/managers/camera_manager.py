from entities.camera_object import *
import threading
import cv2
import time


class camera_managers:

    def __init__(self, rois, paths):
        self.paths = paths
        self.rois = rois
        self.camera_dic = {}

    def display_all(self):
        time.sleep(1)
        while True:
            for object in self.camera_dic:

                cv2.namedWindow(object, cv2.WINDOW_AUTOSIZE)

                image = self.camera_dic[object]["object"].writer_queue.get()
                image = cv2.resize(image, (800, 650))
                cv2.imshow(object, image)
            cv2.waitKey(10)

    def run(self):

        for cam_id in self.rois:
            self.camera_dic[cam_id] = {}
            self.camera_dic[cam_id]["object"] = camera_object(
                self.rois[cam_id], self.paths[cam_id]
            )

        for cam_id in self.camera_dic:
            self.camera_dic[cam_id]["thread"] = threading.Thread(
                target=self.camera_dic[cam_id]["object"].run
            )
            self.camera_dic[cam_id]["thread"].start()

        self.display_all()
