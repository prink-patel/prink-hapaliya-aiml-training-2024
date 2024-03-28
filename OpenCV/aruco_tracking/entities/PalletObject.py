from Database import *


class PalletObject:
    def __init__(
        self,
        id_,
        camera_id,
    ) -> None:
        self.id = id_
        self.camera_id = camera_id
        self.curren_status = None
        self.prevoius_status = None
        self.db_mananger = DBManager()

    def status_(self, status, durationInSeconds):
        self.status = status
        self.durationInSeconds = durationInSeconds
        if not self.curren_status == self.status:
            # print(self.id,"===>",self.curren_status,"--->",self.status)
            self.check_status()
            self.curren_status = self.status

    def check_status(self):
        if self.curren_status == "1" and self.status == "2":
            print(self.durationInSeconds, "in", self.camera_id, self.id)
            database={"video_id":self.camera_id,"aruco_code":self.id,"event_type":"In","event_time":self.durationInSeconds}
            self.db_mananger.enter(database)
            
            
        if self.curren_status == "2" and self.status == "1":
            print(self.durationInSeconds, "out", self.camera_id, self.id)
            database={"video_id":self.camera_id,"aruco_code":self.id,"event_type":"Out","event_time":self.durationInSeconds}
            self.db_mananger.enter(database)
