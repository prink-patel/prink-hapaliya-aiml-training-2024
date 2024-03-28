from Manager.CameraManager import *
from JsonFile import *
from Constant import *
import logging

logging.basicConfig(
    filename="logging_file.log",
    format="%(levelname)s - %(asctime)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger("smart_system")
logger.setLevel(logging.INFO)

class App:

    def __init__(self):
        pass

    def run(self, sources, json_link, model_path):
        
        self.sources = sources
        self.json_link = json_link
        self.model_path = model_path

        roi = JsonFile(json_link)
        desk_roi = (roi.dic_roi())  # return camera name desk name and points in dictionary

        manager = CameraManager(desk_roi, self.sources, self.model_path)
        manager.run()

if __name__ == "__main__":
    app = App()
    app.run(sources, json_link, model_path)

