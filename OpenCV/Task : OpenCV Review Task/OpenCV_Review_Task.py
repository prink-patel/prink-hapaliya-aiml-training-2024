import cv2
import threading
import queue
import numpy as np
import time


class VideoStreamer:
    def __init__(self, src:str) -> None:
        self.src = src     
        self.video = cv2.VideoCapture(self.src)
        self.write_queue = queue.Queue(maxsize=1) 

    def start(self) -> None:
        while True:
            self.capture_video()
    
    def capture_video(self) -> None:
        stat, frame = self.video.read()          
        if stat:
            if self.write_queue.empty():
                self.write_queue.put(frame)       


class BilatFilterClass:
    def __init__(self, capture_queue, d:int=15, sigma_col:int=95, sigma_space:int=95) -> None:
        self.d = d
        self.sigma_col = sigma_col
        self.sigma_space = sigma_space
        self.capture_queue = capture_queue
        self.write_queue = queue.Queue(maxsize=1)
    
    def start(self) -> None:        
        while True:
            self.bilat_filter()

    def bilat_filter(self) -> None:
        if not self.capture_queue.empty():
            frame = self.capture_queue.get()
            frame = cv2.bilateralFilter(frame, d=self.d, sigmaColor=self.sigma_col, sigmaSpace=self.sigma_space)
            self.write_queue.put(frame)
        

class CropperClass:
    def __init__(self, bilat_queue, percent:int=10) -> None:
        self.bilat_queue = bilat_queue
        self.write_queue = queue.Queue(maxsize=1)
        self.percent = percent
        self.prev_frame = None

    def start(self) -> None:
        while True:
            self.crop_frame_bottom()
    
    def crop_frame_bottom(self) -> None:
        if not self.bilat_queue.empty():
            frame = self.bilat_queue.get()
            if self.prev_frame is not None:
                pair = [self.prev_frame]
            else:
                pair = [frame]
            self.prev_frame = frame.copy()
            h = int(((100-self.percent)/100) * frame.shape[0]) 
            frame = frame[:h, :]
            pair.append(frame)
            self.write_queue.put(pair)
            

class DifferClass:
    def __init__(self, crop_queue) -> None:
        self.crop_queue = crop_queue
        self.write_queue = queue.Queue(maxsize=1)
    
    def start(self) -> None:
        while True:
            self.diff_frames()

    def diff_frames(self):
        if not self.crop_queue.empty():
            [frame1, frame2] = self.crop_queue.get()
            frame2 = np.resize(frame2, frame1.shape)
            diff_frame = cv2.absdiff(frame1, frame2)
            self.write_queue.put([frame1, diff_frame])
            

class displayGrid:
    def __init__(self, stream_queues:list) -> None:
        self.stream_queues = stream_queues
    
    def start(self):
        while True:
            self.show()
            
    def show(self):
        while any([stream_queue.empty() for stream_queue in self.stream_queues]):
            time.sleep(0.01)
        main_frame = []
        for stream_queue in self.stream_queues:
            main_frame.append(np.hstack(stream_queue.get()))
        main_frame = np.vstack(main_frame)
        main_frame = cv2.resize(main_frame, (800,800))
        cv2.imshow("Display", main_frame) 
        cv2.waitKey(10)         
            
class StreamManager:




    def __init__(self, links:tuple) -> None:
        self.links = links
        self.storage = {}

        for link in links:
            streamer = VideoStreamer(link)
            bilat_filter = BilatFilterClass(streamer.write_queue)
            cropper = CropperClass(bilat_filter.write_queue)
            differ = DifferClass(cropper.write_queue)
            
            self.storage[link] = {
                "Streamer": {"object": streamer, "thread": threading.Thread(target=streamer.start)},
                "BilatFilter": {"object": bilat_filter, "thread": threading.Thread(target=bilat_filter.start)},
                "Cropper": {"object": cropper, "thread": threading.Thread(target=cropper.start)},
                "Differ": {"object": differ, "thread": threading.Thread(target=differ.start)}
            }
            
            for object_name in self.storage[link]:
                self.storage[link][object_name]["thread"].daemon = True
                self.storage[link][object_name]["thread"].start()
        
        displayer = displayGrid([self.storage[link]["Differ"]["object"].write_queue for link in self.links])
        displayer.start()
# //





if __name__ == "__main__":

    # credentials
    user_name = "test"
    password = "test@1234"

    sources = (
        f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=1&subtype=0",
        f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=4&subtype=0",
        f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=3&subtype=0",
        f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=2&subtype=0"
    )

    SM = StreamManager(sources)

    