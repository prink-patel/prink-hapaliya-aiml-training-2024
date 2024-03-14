import cv2
import numpy as np
import queue
import pandas as pd
from ultralytics import YOLO
from Detection.Tracker import *
from manager.desk_manager import *
from shapely import Point
from database import *


class detect_object:
    def __init__(self, frame_queue, roi) -> None:
        self.frame_queue = frame_queue
        self.writer_queue = queue.Queue(maxsize=1)
        self.roi = roi

        self.person_desk = desk_manager(self.roi)
        self.phone_desk = desk_manager(self.roi)
        self.count_ = 0
        self.db_mananger = DBManager()

    def run(self):
        print("run detect object")
        model = YOLO("best_1.pt")
        class_list = ["person", "phones"]
        tracker = Tracker()
        while True:
            if not self.frame_queue.empty():
                self.frame = self.frame_queue.get()

                results = model.predict(self.frame)

                a = results[0].boxes.data
                a = a.detach().cpu().numpy()
                px = pd.DataFrame(a).astype("float")
                # print(px)

                person_list = []
                phone_list = []
                for index, row in px.iterrows():

                    x1 = int(row[0])
                    y1 = int(row[1])
                    x2 = int(row[2])
                    y2 = int(row[3])
                    d = int(row[5])
                    c = class_list[d]
                    if "person" in c:
                        person_list.append([x1, y1, x2, y2])
                    elif "phones" in c:
                        phone_list.append([x1, y1, x2, y2])

                person_bbox_id = tracker.update(person_list)
                phone_bbox_id = tracker.update(phone_list)
                # print(bbox_id)
                self.person_desk.list_()

                for bbox in person_bbox_id:
                    x3, y3, x4, y4, id = bbox
                    cx = int(x3 + x4) // 2
                    cy = int(y3 + y4) // 2

                    person_center = Point(cx, cy)

                    height, width = self.frame.shape[:2]
                    self.person_desk.run(person_center, height, width)
                    cv2.circle(
                        self.frame, (cx, cy), 4, (0, 0, 255), -1
                    )  # draw ceter points of bounding box
                    cv2.rectangle(
                        self.frame, (x3, y3), (x4, y4), (0, 255, 0), 2
                    )  # Draw bounding box
                    cv2.putText(
                        self.frame,
                        str(id),
                        (cx, cy),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (0, 255, 255),
                        2,
                    )

                self.person_desk.list_diff()

                self.phone_desk.list_()
                for bbox in phone_bbox_id:
                    x3, y3, x4, y4, id = bbox
                    cx = int(x3 + x4) // 2
                    cy = int(y3 + y4) // 2
                    height, width = self.frame.shape[:2]
                    self.phone_desk.run(person_center, height, width)

                    cv2.circle(
                        self.frame, (cx, cy), 4, (0, 0, 255), -1
                    )  # draw ceter points of bounding box
                    cv2.rectangle(
                        self.frame, (x3, y3), (x4, y4), (0, 255, 0), 2
                    )  # Draw bounding box
                    cv2.putText(
                        self.frame,
                        "!?!",
                        (cx, cy),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (0, 255, 255),
                        2,
                    )
                self.phone_desk.list_diff()

                if self.count_ == 125:

                    person_time_values = self.person_desk.find_time_()
                    phone_time_values = self.phone_desk.find_time_()
                    self.db_mananger.enter("Overall Occupancy", person_time_values)
                    self.db_mananger.enter("Mobile Usage",phone_time_values)

                    self.count_ = 0
                else:
                    self.count_ = self.count_ + 1

                if self.writer_queue.empty():
                    self.writer_queue.put(self.frame)
