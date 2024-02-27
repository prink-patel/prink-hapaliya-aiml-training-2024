import json
from constants import *
from data_filter import *

from managers.camera_managers import *


class app:
    def __init__(self) -> None:
        json_path_for_filter = "/home/wot-prink/Desktop/hello/OpenCV/Trailer/trailer_yard.camera_rois-65dc30dedcdf0.json"
        
        data_points1={}
        data_points={}
        dic_data = data_filter(json_path_for_filter, [903,904,905,906])
        dics_data = dic_data.run()
        
        for j in dics_data:
            
            for i, video in enumerate(dics_data[j]):
                data_points1[dics_data[j][i]["roi"]]=dics_data[j][i]["points_norm"]
                
            data_points[j]=data_points1
            data_points1={}
        
        # for j in dics_data:
        #     print(data_points[j])
        #     print()
            
        camera_managers(video_dic,data_points)


app()

