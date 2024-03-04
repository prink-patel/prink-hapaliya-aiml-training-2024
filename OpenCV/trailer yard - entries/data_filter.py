import json
import os


class ExtractData:

    def __init__(self, jaso_link, camera_ids):
        self.jaso_link = jaso_link
        self.camera_ids = camera_ids

    def data_paths(self):
        self.paths = {}
        for camera_id in self.camera_ids:
            img_path = os.path.join(
                "/home/wot-prink/Desktop/hello/OpenCV/trailer1/camera_images-65dc30c421274",
                camera_id + ".jpg",
            )
            self.paths[camera_id] = {}
            self.paths[camera_id]["img_path"] = img_path

        self.paths["MRKDC_0984_0903"][
            "json_path"
        ] = "/home/wot-prink/Desktop/hello/OpenCV/trailer1/trailer_entries-65dc30a819989/MRKDC_0984_0903__01_13_2024_05_59_03_500_AM_UTC-05_00_01132024.json"
        self.paths["MRKDC_0984_0904"][
            "json_path"
        ] = "/home/wot-prink/Desktop/hello/OpenCV/trailer1/trailer_entries-65dc30a819989/MRKDC_0984_0904__01_13_2024_05_59_03_500_AM_UTC-05_00_01132024.json"
        self.paths["MRKDC_0984_0905"][
            "json_path"
        ] = "/home/wot-prink/Desktop/hello/OpenCV/trailer1/trailer_entries-65dc30a819989/MRKDC_0984_0905__01_13_2024_05_59_03_500_AM_UTC-05_00_01132024.json"
        self.paths["MRKDC_0984_0906"][
            "json_path"
        ] = "/home/wot-prink/Desktop/hello/OpenCV/trailer1/trailer_entries-65dc30a819989/MRKDC_0984_0906__01_13_2024_05_59_03_500_AM_UTC-05_00_01132024.json"

    def run(self):
        camera_name = "MRKDC_0984_0" 
        self.camera_ids = [
            camera_name + str(camera_id) for camera_id in self.camera_ids
        ]
        camera_data_rois = {}
        f = open(self.jaso_link)
        all_data = json.load(f)
        for data in all_data:
            if data["cam_name"] in self.camera_ids:
                if data["cam_name"] not in camera_data_rois.keys():
                    camera_data_rois[data["cam_name"]] = []
                    camera_data_rois[data["cam_name"]].append(data)
                else:
                    camera_data_rois[data["cam_name"]].append(data)

        self.data_paths()

        return camera_data_rois, self.paths
