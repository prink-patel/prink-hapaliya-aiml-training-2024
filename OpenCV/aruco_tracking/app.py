import json
from constants import *
from managers.VideoManager import *



json_path = open("/home/wot-prink/Downloads/aruco_tracking-20240223T114103Z-001/aruco_tracking/data.json")
data = json.load(json_path)
for i, video in enumerate(video_dic):
    video_dic[video]["rois"] = data[i]["rois"]

# print(video_list)
VideoManager(video_dic)




























# for video_data in video_list:
#     print(video_data)
# data = video_list["video1"]
# print(data["url"])
# print(data["rois"])
