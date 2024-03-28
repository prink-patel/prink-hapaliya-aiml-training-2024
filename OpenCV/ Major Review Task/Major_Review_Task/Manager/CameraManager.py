import threading
import cv2
import time
from Object.CameraObject import *
from Object.DetectObject import *
from Constant import *
import logging
logger = logging.getLogger("smart_system")

class CameraManager:
    
    def __init__(self, desk_roi, sources,model_path):
        logger.info(f"call {__name__}")
        self.sources = sources
        self.desk_roi = desk_roi
        self.model_path=model_path
        self.camera_dict = {}
        
    # create class Object and than start thread in object function
    def run(self):
        logger.info(f"run {__name__}")
        # check values is valid or not
        if len(self.sources)==0:
            logger.critical(f"sources link is empty")
        elif self.desk_roi==None:
            logger.critical(f"desk_roi is empty")
        elif len(self.model_path)==0:
            logger.critical(f"model path is empty")
        else:
            # create object and store in dictionary
            for camera_id in self.sources:
                self.camera_dict[camera_id] = {}
                self.camera_dict[camera_id]["get_cap"] = {
                    "object": CameraObject(
                        camera_id, self.desk_roi[camera_id], self.sources[camera_id]
                    ),
                    "thread": None,
                }
                self.camera_dict[camera_id]["detect_object"] = {
                    "object": DetectObject(
                        self.camera_dict[camera_id]["get_cap"]["object"].writer_queue,
                        self.desk_roi[camera_id],self.model_path
                    ),
                    "thread": None,
                }
            
            # start thread 
            for camera_id in self.sources:
                for object_dict in self.camera_dict[camera_id]:
                    self.camera_dict[camera_id][object_dict]["thread"] = threading.Thread(
                        target=self.camera_dict[camera_id][object_dict]["object"].run
                    )
                    self.camera_dict[camera_id][object_dict]["thread"].start()
            if DISPLAY_FLAG:
                self.display_all()

    # display all camera 
    def display_all(self):
        time.sleep(1)
        while True:
            for object in self.camera_dict:
                cv2.namedWindow(object, cv2.WINDOW_AUTOSIZE)
                image = self.camera_dict[object]["detect_object"]["object"].writer_queue.get()
                image = cv2.resize(image, (800, 650))
                cv2.imshow(object, image)
            cv2.waitKey(1)
