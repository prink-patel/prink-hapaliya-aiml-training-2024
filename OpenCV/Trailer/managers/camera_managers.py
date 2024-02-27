import threading
import sys
import cv2
import time
sys.path.insert(1, "/home/wot-prink/Desktop/hello/OpenCV/Trailer/entities")
from camera_object import *


class camera_managers:
    print("camera_manager")
    def __init__(self, video_dic,dics_data):
        self.video_dic = video_dic
        self.dics_data=dics_data
        self.camera_objects = {}
        
        print("working -1")
        self.video_langth=len(self.video_dic)
        i=903
        # print(dics_data[f"MRKDC_0984_0{904}"])
        for video_data in video_dic:
            self.video_dic[video_data]["object"] = camera_object(
                video_dic[video_data],dics_data[f"MRKDC_0984_0{i}"],i
                
            )
            i=i+1
            
        for video_data in video_dic:
            self.video_dic[video_data]["thread"] = threading.Thread(
                target=self.video_dic[video_data]["object"].run
            )
            self.video_dic[video_data]["thread"].start()

            print("working -2")
        self.display_all()
        
        
    def display_all(self):
        time.sleep(1)
        while True:
            for object in self.video_dic:

                cv2.namedWindow(object, cv2.WINDOW_AUTOSIZE)

                image = self.video_dic[object]["object"].write_queue.get()
                image = cv2.resize(image, (800, 650))
                cv2.imshow(object, image)
            cv2.waitKey(10)   
            
            
    
        
        # cv2.imshow(f"{self.data}", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
