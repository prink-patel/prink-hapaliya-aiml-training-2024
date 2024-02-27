import sys

sys.path.insert(
    1,
    "/home/wot-prink/Downloads/aruco_tracking-20240223T114103Z-001/aruco_tracking/entities",
)
from VideoObject import *
import cv2


class VideoManager:

    def __init__(self, video_dic):
        self.video_dic = video_dic
        print("working -1")

        for video_data in video_dic:
            self.video_dic[video_data]["object"] = VideoObject(
                video_data, video_dic[video_data], self.database
            )
        for video_data in video_dic:
            self.video_dic[video_data]["thread"] = threading.Thread(
                target=self.video_dic[video_data]["object"].do
            )
            self.video_dic[video_data]["thread"].start()

            print("working -2")
