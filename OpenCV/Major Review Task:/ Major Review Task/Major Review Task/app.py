# from data_filter import *
import json
from manager.camera_manager import *
from json_file import *


class App:

    def __init__(self):
        pass

    def run(self, sources):
        self.sources = sources
        roi = json_file(
            "/home/wot-prink/Desktop/hello/he/ Major Review Task/roi.json"
        )
        dic_roi = roi.dic_roi()
        manager = camera_manager(dic_roi, self.sources)
        manager.run()


if __name__ == "__main__":
    app = App()

    user_name = "test"
    password = "test@1234"

    sources = {
        # "camera_1": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=1&subtype=0",
        "camera_2": f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=2&subtype=0",
        # "camera_4": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=4&subtype=0",
        # "camera_3": f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=3&subtype=0",
    }
    app.run(sources)
