from data_filter import *
from managers.camera_manager import *

import logging

logging.basicConfig(
    filename="logging_file.log",
    format="%(levelname)s - %(asctime)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class App:

    def __init__(self):
        pass

    def run(self):

        jaso_link = "/home/wot-prink/Desktop/hello/OpenCV/trailer1/trailer_data/trailer_yard.camera_rois-65dc30dedcdf0.json"
        camera_ids = [903, 904, 905, 906]

        extracted_data = ExtractData(jaso_link, camera_ids)

        rois, paths = extracted_data.run()
        cam_manager = camera_managers(rois, paths)
        cam_manager.run()


if __name__ == "__main__":
    app = App()
    app.run()
