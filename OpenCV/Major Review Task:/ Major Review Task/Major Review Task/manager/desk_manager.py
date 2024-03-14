from cam_object.desk_obj import *
from shapely import Polygon


class desk_manager:
    def __init__(self, roi) -> None:
        self.roi = roi
        self.roi_obj_dic = {}
        self.status = False

        for desk_name in roi.keys():
            if desk_name not in self.roi_obj_dic.keys():
                self.roi_obj_dic[desk_name] = [desk_obj(desk_name), self.status]
        # print(self.roi_obj_dic)
        self.pre_desk_list = []
        self.curr_desk_list = []
        self.count_desk_list = []

    def list_(self):
        self.desk_list = []
        self.pre_desk_list = self.curr_desk_list
        self.curr_desk_list = self.desk_list

    def run(self, person_center, height, width):
        self.person_center = person_center
        self.height = height
        self.width = width

        for desk_name, val in self.roi.items():
            if desk_name not in [
                "nonworking_space",
                "working_space_1",
                "working_space_2",
                "door",
            ]:
                # print("--------------")
                # print(desk_name)

                coord = np.array(val)
                c = np.array([self.width, self.height])
                final_coord = np.array(coord * c, dtype="int64")

                disk_area = Polygon(final_coord)
                if self.person_center.within(disk_area):
                    if desk_name not in self.desk_list:
                        self.desk_list.append(desk_name)
                    if self.roi_obj_dic[desk_name][1] is False:
                        self.roi_obj_dic[desk_name][1] = True
                        self.roi_obj_dic[desk_name][0].run()

    def list_diff(self):
        # print(self.curr_desk_list,"<======>",self.pre_desk_list)
        for find_missing_disk in self.pre_desk_list:
            if find_missing_disk not in self.curr_desk_list:

                self.count_desk_list.append(find_missing_disk)

        if len(self.count_desk_list) > 0:
            for desk_name in self.count_desk_list:
                if desk_name not in self.curr_desk_list:
                    count_frame = self.roi_obj_dic[desk_name][0].count_frame1()
                    if count_frame:
                        # print(desk_name)
                        self.roi_obj_dic[desk_name][0].stope_time()
                        self.roi_obj_dic[desk_name][1] = False
                        self.count_desk_list.remove(desk_name)

    def find_time_(self):
        database_values = {}
        for desk_name in self.roi_obj_dic:
            print(desk_name, end="")
            database_values[desk_name]= self.roi_obj_dic[desk_name][0].count_time()
        return database_values