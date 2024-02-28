from entities.truck_object import *

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class truck_manager:
    def __init__(self, camera_id, json_data) -> None:
        self.camera_id = camera_id
        self.json_data = json_data
        self.current_truck = {}
        self.tracked_truck = {}
        self.old_truck = {}

    def dictionary_manage(self, frame_with_id):
        self.frame_with_id = frame_with_id

        for obj_str in self.json_data["messages"][self.frame_with_id]["objects"]:
            obj_data = obj_str.split("|")
            if obj_data[0] == "TOP":
                truck_id = obj_data[1]
                if truck_id not in self.tracked_truck:
                    if truck_id not in self.old_truck:
                        self.current_truck[truck_id] = truck_object(truck_id)

                    else:
                        temp_object = self.old_truck.pop(truck_id)
                        self.current_truck[truck_id] = temp_object
                        self.current_truck[truck_id].count_reset()

                else:
                    self.current_truck[truck_id] = self.tracked_truck[truck_id]

        for truck_id in self.old_truck:
            self.old_truck[truck_id].count_add()

        for truck_id in list(self.tracked_truck.keys()):
            if truck_id not in self.current_truck:
                temp_object = self.tracked_truck.pop(truck_id)
                self.old_truck[truck_id] = temp_object

        self.delete_missing_truck(max_number_of_frame=50)

        self.tracked_truck = self.current_truck 

        logger.info("----------------------------------------------------------------------------------------------------------------------------------------------")
        logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Current trucks :{list(self.current_truck.keys())}")
        logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Old trucks     :{list(self.old_truck.keys())}")
        logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Tracked trucks :{list(self.tracked_truck.keys())}")
        logger.info("-----------------------------------------------------------------------------------------------------------------------------------------------")
        self.current_truck = {}
        
        
    def delete_missing_truck(self, max_number_of_frame):

        for truck_id in list(self.old_truck.keys()):
            if self.old_truck[truck_id].check_count(max_number_of_frame):
                del self.old_truck[truck_id]
                logger.warning(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Truck is missing for more than {max_number_of_frame} frames so delete truck id:{truck_id} ")
