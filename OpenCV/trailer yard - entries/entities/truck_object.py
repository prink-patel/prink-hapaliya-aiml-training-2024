from shapely.geometry import Point, LineString, Polygon

from database import DBManager
import threading


class truck_object:
    def __init__(self, img_copy, truck_id, obj_data) -> None:
        self.img_copy = img_copy
        self.truck_id = truck_id
        self.count = 0
        self.obj_data = obj_data
        # self.current_2 = self.find_points(self.truck_id, self.obj_data)
        # self.current_1=None
        self.current_loc = None
        # self.next1()
        self.db_mananger = DBManager()

    # def next1(self):

    #     self.current_loc=self.current_1
    #     self.current_1=self.current_2

    def count_reset(self):
        self.count = 0

    def count_add(self):
        self.count = self.count + 1

    def check_count(self, max_number=50):
        if self.count > max_number:
            return True
        else:
            return False

    def run(self, time, img_copy, coord_dic, camera_name, frame_id, obj_data):
        self.obj_data = obj_data
        self.time = time
        self.img_copy = img_copy
        self.coord_dic = coord_dic
        self.camera_name = camera_name
        self.frame_id = frame_id
        self.prev_loc = self.current_loc
        self.current_loc = self.find_points(self.truck_id, self.obj_data)


        self.trigger_event(self.prev_loc, self.current_loc)

    def trigger_event(self, previous, current):
        event_type = None
        if previous == current:
            return

        if previous is None and current == "ROAD":
            event_type = "IN"

        elif previous == "ROAD" and current is None:
            event_type = "OUT"

        elif previous == "ROAD" and current in ["TPP", "DPP"]:
            event_type = "PARKED"

        elif previous in ["TPP", "DPP"] and current == "ROAD":
            event_type = "UNPARKED"

        if event_type is not None:
            # print(self.camera_name,"------->",self.truck_id,"===",event_type)

            if event_type in ["IN", "OUT"]:
                location = None
            elif event_type == "PARKED":
                location = self.current_loc

            elif event_type == "UNPARKED":
                location = self.prev_loc
            self.store_event(event_type, location)

    def store_event(self, event_type, location):
        data = {
            "trailer_id": self.truck_id,
            "camera_name": self.camera_name,
            "event_type": event_type,
            "location": location,
            "event_time": self.time,
        }
        threading.Thread(target=self.db_mananger.enter, args=[data]).start()
        
    def find_points(self, truck_id, obj_data):
        self.obj_data = obj_data
        self.truck_id = truck_id
        x1 = self.obj_data[3]
        y1 = self.obj_data[4]
        x2 = self.obj_data[5]
        y2 = self.obj_data[6]

        height, width = self.img_copy.shape[:2]

        x1 = int(x1) * width // 10000
        x2 = int(x2) * width // 10000
        y1 = int(y1) * height // 10000
        y2 = int(y2) * height // 10000
        center = (x2 + x1) // 2, (y2 + y1) // 2

        parent = None
        self.truck_cent = Point(center)
        for i in self.coord_dic.keys():
            c = Polygon(self.coord_dic[i])
            if c.contains(self.truck_cent):
                parent = i
        return parent
