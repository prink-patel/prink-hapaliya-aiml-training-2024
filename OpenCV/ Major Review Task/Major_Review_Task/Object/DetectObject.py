import cv2
import queue
import pandas as pd
from ultralytics import YOLO
from Detection.Tracker import *
from Manager.DeskManager import *
from shapely import Point
from Database import *
from datetime import datetime
import logging
logger = logging.getLogger("smart_system")

class DetectObject:
    
    def __init__(self, frame_queue, roi,model_path) -> None:
        logger.info(f"call {__name__}")
        self.frame_queue = frame_queue
        self.roi = roi
        self.model_path=model_path
        self.writer_queue = queue.Queue(maxsize=1)
        self.person_desk = DeskManager(self.roi)
        self.phone_desk = DeskManager(self.roi)
        self.db_mananger = DBManager()
        self.count_ = 0

    def run(self):
        
        logger.info(f"run {__name__}")
        model = YOLO(self.model_path)
        class_list = ["Phone"]
        
        tracker = Tracker()
        
        while True:
            if not self.frame_queue.empty():
                self.frame = self.frame_queue.get()

                results = model.predict(self.frame)
                a = results[0].boxes.data
                a = a.detach().cpu().numpy()
                px = pd.DataFrame(a).astype("float")

                person_list = [] #store bounding box points values for person
                phone_list = [] #store bounding box points values for phone
                for index, row in px.iterrows():
                    x1 = int(row[0])
                    y1 = int(row[1])
                    x2 = int(row[2])
                    y2 = int(row[3])
                    d = int(row[5])
                    c = class_list[d]
                    if "person" in c:
                        person_list.append([x1, y1, x2, y2])
                    elif "Phone" in c:
                        phone_list.append([x1, y1, x2, y2])

                person_bbox_id = tracker.update(person_list)
                phone_bbox_id = tracker.update(phone_list)
                
                self.person_desk.list_() # find all desk to working perosn 
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
                self.person_desk.list_diff() # find defference to person current and pervious working for all desk

                self.phone_desk.list_() # find all desk to used phone  
                for bbox in phone_bbox_id:
                    x3, y3, x4, y4, id = bbox
                    cx = int(x3 + x4) // 2
                    cy = int(y3 + y4) // 2
                    phone_center = Point(cx, cy)
                    height, width = self.frame.shape[:2]
                    self.phone_desk.run(phone_center, height, width)
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
                self.phone_desk.list_diff() # find defference to current and pervious phone used for all desk
                
                
                myobj = datetime.now()
                if myobj.second==0 and self.count_==0: # store values in date or time wise in database
                    logger.info(f"--------------------------------------------")
                    logger.info("save in database")
                    logger.info("---------------------------------------------")
                    person_time_values = self.person_desk.find_time_() #find total time working person on desk
                    phone_time_values = self.phone_desk.find_time_()    #find total time used phone on desk
                    self.db_mananger.enter("Overall Occupancy", person_time_values)
                    self.db_mananger.enter("Mobile Usage", phone_time_values)
                    self.count_ = 1
                    
                elif myobj.second==1:
                    self.count_ = 0

                if self.writer_queue.empty():
                    self.writer_queue.put(self.frame)
