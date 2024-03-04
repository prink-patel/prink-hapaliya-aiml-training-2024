from entities.truck_object import *
from shapely.geometry import Point, LineString, Polygon
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

    def dictionary_manage(self, frame_with_id, coord_dic, img_copy):
        self.frame_with_id = frame_with_id
        self.coord_dic = coord_dic
        self.img_copy = img_copy
        self.previous_truck_roi = None
        for obj_str in self.json_data["messages"][self.frame_with_id]["objects"]:
            self.time=self.json_data["messages"][self.frame_with_id]["ts"]
            self.camera_name = self.json_data["messages"][self.frame_with_id]["sensor"]
            self.obj_data = obj_str.split("|")
            if self.obj_data[0] == "TOP":
                truck_id = self.obj_data[1]
                # self.current_truck_center_points=self.find_points(self.camera_id,obj_data)

                if truck_id not in self.tracked_truck:
                    if truck_id not in self.old_truck:
                        self.current_truck[truck_id] = truck_object(
                            self.img_copy, truck_id, self.obj_data
                        )

                    else:
                        temp_object = self.old_truck.pop(truck_id)
                        self.current_truck[truck_id] = temp_object
                        self.current_truck[truck_id].count_reset()

                else:
                    self.current_truck[truck_id] = self.tracked_truck[truck_id]
                    
                self.current_truck[truck_id].run(self.time,self.img_copy, self.coord_dic,self.camera_name,self.frame_with_id,self.obj_data)

        
        for truck_id in self.old_truck:
            self.old_truck[truck_id].count_add()

        for truck_id in list(self.tracked_truck.keys()):
            if truck_id not in self.current_truck:
                temp_object = self.tracked_truck.pop(truck_id)
                self.old_truck[truck_id] = temp_object
                # print(self.camera_id,"out--->",truck_id)

        self.delete_missing_truck(max_number_of_frame=50)
        for truck_id in self.current_truck.keys():
            # self.current_truck[truck_id].run(self.img_copy,self.coord_dic)
            if truck_id not in self.tracked_truck.keys():
                self.value = self.json_data["messages"][self.frame_with_id]["objects"]

                # print(self.camera_id,"in---->",truck_id)
        self.tracked_truck = self.current_truck
        
        


        # logger.info("----------------------------------------------------------------------------------------------------------------------------------------------")
        # logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Current trucks :{list(self.current_truck.keys())}")
        # logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Old trucks     :{list(self.old_truck.keys())}")
        # logger.info(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Tracked trucks :{list(self.tracked_truck.keys())}")
        # logger.info("-----------------------------------------------------------------------------------------------------------------------------------------------")
        self.current_truck = {}

    def delete_missing_truck(self, max_number_of_frame):
        for truck_id in list(self.old_truck.keys()):
            if self.old_truck[truck_id].check_count(max_number_of_frame):
                del self.old_truck[truck_id]
                # logger.warning(f"Camera_id :{self.camera_id} | frame id :{self.frame_with_id} | timestamp {self.json_data["messages"][self.frame_with_id]["ts"]} | Truck is missing for more than {max_number_of_frame} frames so delete truck id:{truck_id} ")

    # def find_points(self,truck_id,obj_data):
    #     self.obj_data=obj_data
    #     self.truck_id=truck_id
    #     self.truck_roi=None
    #     x1 = self.obj_data[3]
    #     y1 = self.obj_data[4]
    #     x2 = self.obj_data[5]
    #     y2 = self.obj_data[6]

    #     height, width = self.img_copy.shape[:2]

    #     x1 = int(x1) * width // 10000
    #     x2 = int(x2) * width // 10000
    #     y1 = int(y1) * height // 10000
    #     y2 = int(y2) * height // 10000
    #     center=(x2 + x1)/2, (y2+y1)/2

    #     # self.truck_roi = Point(center)
    #     self.check_area(center)

    # def check_area(self,truck_roi):
    #     self.truck_roi=truck_roi
    #     self.truck_cent=Point(self.truck_roi)
    #     for i in self.coord_dic.keys():
    #         c = Polygon(self.coord_dic[i])
    #         if self.truck_cent.intersection(c):
    #             return i

    # road_coord=self.coord_dic["TPP"]
    # c = Polygon(road_coord)
    # intersect = self.truck_roi.intersection(c).area / self.truck_roi.union(c).area
    # intersect_round=round(intersect*100, 2), '%'
    # print(intersect_round)
    # if intersect>0.0051:


# if truck_id not in self.current_truck.keys():
#     self.current_truck[truck_id] = truck_object(truck_id,obj_data)
# if self.frame_with_id>1:
#     for previous_loc in self.json_data["messages"][self.frame_with_id-1]["objects"]:
#         previous_loc_list = previous_loc.split("|")
#         if previous_loc_list[0]=="top" and previous_loc_list[1]==truck_id:

#             self.previous_truck_center_points=self.find_points(self.camera_id,previous_loc_list)
#             self.previous_truck_roi=self.check_area(self.previous_truck_center_points)
#             self.count=1
# # if self.count!=1:
# #     self.previous_truck_roi=None
# # else:
# #     self.count=0
# self.current_truck_center_points=self.find_points(self.camera_id,obj_data)
# self.current_truck_roi=self.check_area(self.current_truck_center_points)
# if self.current_truck_roi!=self.previous_truck_roi:
#     print(self.current_truck_roi,"----->",self.previous_truck_roi)
# if truck_posz=="ROAD":
#     print(truck_posz)
# self.current_truck=obj_data
