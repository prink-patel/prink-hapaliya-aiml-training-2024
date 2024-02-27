import json
import os


class data_filter:

    def __init__(self, file_path, camera_ids):
        self.file_path = file_path
        self.camera_ids = camera_ids
        
    def run(self):
        camera_name = "MRKDC_0984_0" 
        self.camera_ids = [
            camera_name + str(camera_id) for camera_id in self.camera_ids
        ] 
        camera_data_rois = {}

        f = open(self.file_path)
        all_data = json.load(f)

        # filter data using camera ids
        for data in all_data:
            if data["cam_name"] in self.camera_ids:
                if data["cam_name"] not in camera_data_rois.keys():
                    camera_data_rois[data["cam_name"]] = []
                    camera_data_rois[data["cam_name"]].append(data)
                else:
                    camera_data_rois[data["cam_name"]].append(data)

        return camera_data_rois

