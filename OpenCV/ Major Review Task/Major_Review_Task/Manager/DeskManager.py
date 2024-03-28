from Object.DeskObject import *
from shapely import Polygon
import numpy as np
import logging
logger = logging.getLogger("smart_system")

class DeskManager:
    
    def __init__(self, roi) -> None:
        logger.info(f"call {__name__}")
        self.roi = roi
        self.roi_obj_dic = {} # store all new desk on diction and also object
        self.status = False # used to check current desk status 

        # store all new desk in dictionary key and object and status store in values
        for desk_name in roi.keys():
            if desk_name not in self.roi_obj_dic.keys():
                self.roi_obj_dic[desk_name] = [DeskObject(desk_name), self.status]
        self.pre_desk_list = []
        self.curr_desk_list = []
        self.count_desk_list = []

    # update current and previous desk list
    def list_(self):
        self.desk_list = []
        self.pre_desk_list = self.curr_desk_list
        self.curr_desk_list = self.desk_list

    def run(self, person_center, height, width):
        logger.info(f"run {__name__}")
        self.person_center = person_center
        self.height = height
        self.width = width

        for desk_name, val in self.roi.items():
            if desk_name not in ["nonworking_space","working_space_1","working_space_2","door"]:
                coord = np.array(val)
                c = np.array([self.width, self.height])
                final_coord = np.array(coord * c, dtype="int64")

                disk_area = Polygon(final_coord)
                if self.person_center.within(disk_area):
                    # desk name not in desk list so update desk list 
                    if desk_name not in self.desk_list:
                        self.desk_list.append(desk_name)
                    # check status to start time count
                    if self.roi_obj_dic[desk_name][1] is False:
                        self.roi_obj_dic[desk_name][1] = True
                        self.roi_obj_dic[desk_name][0].run()
    
    # check different current desk and previouse desk to check in 5 frame not found than stope time count
    def list_diff(self):
        for find_missing_disk in self.pre_desk_list:
            if find_missing_disk not in self.curr_desk_list:
                self.count_desk_list.append(find_missing_disk)

        if len(self.count_desk_list) > 0:
            for desk_name in self.count_desk_list:
                if desk_name not in self.curr_desk_list:
                    count_frame = self.roi_obj_dic[desk_name][0].count_frame1() #count frame 5 frame object not detect
                    if count_frame:
                        self.roi_obj_dic[desk_name][0].stope_time() # stope time 
                        self.roi_obj_dic[desk_name][1] = False  # status change so next time detect start count 
                        self.count_desk_list.remove(desk_name)  # remove count desk list

    # reture total count time with desk name 
    def find_time_(self):
        database_values = {}
        for desk_name in self.roi_obj_dic:
            database_values[desk_name]= self.roi_obj_dic[desk_name][0].count_time()
        return database_values