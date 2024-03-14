import numpy as np
import cv2
import queue
import time


class desk_obj:
    def __init__(self, desk_name) -> None:
        self.desk_name = desk_name
        self.cal_time = 0
        self.count_frame=0
        self.begin=0
        self.end=0

    def run(self):
        self.begin = time.time()
        print(self.desk_name)

    def stope_time(self):
        self.end = time.time()
        self.total = self.end - self.begin
        val=self.update_time()

    def update_time(self):
        self.cal_time = self.cal_time + self.total
        print("----------",self.cal_time)
        print("----------------------------")
        return self.cal_time

    def count_frame1(self):
        if self.count_frame<5:
            self.count_frame=self.count_frame+1
            
            return False
        else:
            self.count_frame=0
            return True

    def count_time(self):
        if self.begin>0:
            self.end = time.time()
        self.total = self.end - self.begin
        return self.update_time()