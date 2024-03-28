import time
import logging
logger = logging.getLogger("smart_system")


class DeskObject:
    def __init__(self, desk_name) -> None:
        logger.info(f"call {__name__}")
        self.desk_name = desk_name
        self.cal_time = 0
        self.count_frame=0
        self.begin=0
        self.end=0

    # start time count
    def run(self):
        logger.info(f"run {__name__}")
        self.begin = time.time()

    # stope time count 
    def stope_time(self):
        if self.begin==0:
            self.end=0
        else:
            self.end = time.time()
        self.total = self.end - self.begin
        val=self.update_time()
        self.begin=0
        self.end=0

    # total time calculate 
    def update_time(self):
        self.cal_time = self.cal_time + self.total
        return self.cal_time

    # count frame 
    def count_frame1(self):
        if self.count_frame<5:
            self.count_frame=self.count_frame+1
            return False
        else:
            self.count_frame=0
            return True

    # count total time 
    def count_time(self):
        if self.begin>0:
            end = time.time()
        elif self.begin==0:
            end=0
        self.total = end - self.begin
        return self.update_time()