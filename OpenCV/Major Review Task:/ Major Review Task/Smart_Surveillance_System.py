import cv2
import threading
import queue
import numpy as np
import time


class VideoStreamer:
    def __init__(self, src: str) -> None:
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


class displayGrid:
    def __init__(self, stream_queues: list) -> None:
        self.stream_queues = stream_queues

    def start(self):
        while True:
            self.show()

    def show(self):
        while any([stream_queue.empty() for stream_queue in self.stream_queues]):
            time.sleep(0.01)
        main_frame = []
        for stream_queue in self.stream_queues:
            # main_frame.append(np.hstack(stream_queue.get()))
            main_frame.append(np.vstack(stream_queue.get()))
            
        main_frame = cv2.resize(main_frame, (800, 800))
        cv2.imshow("Display", main_frame)
        cv2.waitKey(10)
        
        
        
class StreamManager:
    def __init__(self, links: tuple) -> None:
        self.links = links
        self.storage = {}

        for link in links:
            streamer = VideoStreamer(link)
            # bilat_filter = BilatFilterClass(streamer.write_queue)
            # cropper = CropperClass(bilat_filter.write_queue)
            # differ = DifferClass(cropper.write_queue)

            self.storage[link] = {
                "Streamer": {
                    "object": streamer,
                    "thread": threading.Thread(target=streamer.start),
                },
                # "BilatFilter": {
                #     "object": bilat_filter,
                #     "thread": threading.Thread(target=bilat_filter.start),
                # },
                # "Cropper": {
                #     "object": cropper,
                #     "thread": threading.Thread(target=cropper.start),
                # },
                # "Differ": {
                #     "object": differ,
                #     "thread": threading.Thread(target=differ.start),
                # },
            }

            for object_name in self.storage[link]:
                self.storage[link][object_name]["thread"].daemon = True
                self.storage[link][object_name]["thread"].start()

        displayer = displayGrid(
            [
                self.storage[link]["Streamer"]["object"].write_queue
                for link in self.links
            ]
        )
        displayer.start()


import cv2

if __name__ == "__main__":

    # credentials
    user_name = "test"
    password = "test@1234"

    sources = (
        f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=1&subtype=0",
        # f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=4&subtype=0",
        # f"rtsp://test:{password}@192.168.44.245:554/cam/realmonitor?channel=3&subtype=0",
    )
    SM = StreamManager(sources)
