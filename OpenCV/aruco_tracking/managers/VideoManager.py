from entities.VideoObject import *
import threading
import time

class VideoManager:
    def __init__(self, url, json_dic) -> None:
        self.url = url
        self.json_dic = json_dic
        self.camera_dic = {}

    def run(self):
        print("video_manager run")

        for camera_id in self.url:
            self.camera_dic[camera_id] = {}
            self.camera_dic[camera_id]["object"] = VideoObject(
                camera_id, self.url[camera_id], self.json_dic[camera_id]
            )
        for camera_id in self.url:
            self.camera_dic[camera_id]["thread"] = threading.Thread(
                target=self.camera_dic[camera_id]["object"].run
            )
            self.camera_dic[camera_id]["thread"].start()
        
        
        self.display_all()
        
        
        
    def display_all(self):
        time.sleep(1)
        while True:
            for object in self.camera_dic:

                cv2.namedWindow(object, cv2.WINDOW_AUTOSIZE)

                image = self.camera_dic[object]["object"].writer_queue.get()
                image = cv2.resize(image, (800, 650))
                cv2.imshow(object, image)
            cv2.waitKey(40)