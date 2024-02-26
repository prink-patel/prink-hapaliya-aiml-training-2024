import sys
sys.path.insert(1,"/home/wot-prink/Downloads/aruco_tracking-20240223T114103Z-001/aruco_tracking/entities")
from VideoObject import *
import cv2


class VideoManager:

    def __init__(self, video_dic):
        self.video_dic = video_dic
        print("working -1")

        for video_data in video_dic:
            self.video_dic[video_data]["object"] = VideoObject(video_dic[video_data])
            self.video_dic[video_data]["object"].detect()
            print("working -2")
       