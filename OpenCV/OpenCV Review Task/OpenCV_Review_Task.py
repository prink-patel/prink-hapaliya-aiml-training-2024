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
        stat, frame = self.video.read()  # read a frame from the video
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
            main_frame.append(stream_queue.get())
        main_frame = np.vstack(main_frame)
        main_frame = cv2.resize(main_frame, (800, 800))
        cv2.imshow("Display", main_frame)
        cv2.waitKey(10)


class manager:
    def __init__(self, urls):
        self.urls = urls
        self.store = {}
        for i in urls:
            self.store[i] = {}
            stram = VideoStreamer(i)
            self.store[i]["streamer"] = {"object": stram, "thread": None}

        for _, rtps in enumerate(self.urls):
            for object in self.store[rtps]:
                self.store[rtps][object]["thread"] = threading.Thread(
                    target=self.store[rtps][object]["object"].start
                )

                self.store[rtps][object]["thread"].daemon = True
                self.store[rtps][object]["thread"].start()

        displayer = displayGrid(
            [self.store[link]["streamer"]["object"].write_queue for link in self.urls]
        )
        displayer.start()


if __name__ == "__main__":

    # credentials
    user_name = "test"
    password = "test@1234"

    sources = [
        f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=1&subtype=0",
        f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=4&subtype=0",
        f"rtsp://{user_name}:{password}@192.168.44.245:554/cam/realmonitor?channel=3&subtype=0",
    ]

    SM = manager(sources)
