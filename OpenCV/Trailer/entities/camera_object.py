import numpy as np
import urllib
import cv2
import sys
from shapely.geometry import Point, LineString, Polygon
import queue

# from managers.trailer_manager import trailer_manager

from managers.trailer_manager import *

# sys.path.insert(1, "/home/wot-prink/Desktop/hello/OpenCV/Trailer")
# from display import *


class camera_object:

    def __init__(self, data, dics_data, i):
        self.data = data
        self.url = data["url"]
        self.roi_points = dics_data
        self.i = i
        self.write_queue = queue.Queue(maxsize=1)

        print("camera_object")

    def run(self):

        # print(self.roi_points,"---->",self.i)
        
        self.dic_img = {}
        self.roi1 = self.roi_points["TPP"]
        self.roi2 = self.roi_points["DPP"]
        self.roi3 = self.roi_points["ROAD"]
        image = cv2.imread(self.url)

        self.height, self.width = image.shape[:2]
        self.roi_1 = (self.roi1 * np.array([self.width, self.height])).astype("int64")
        self.roi_2 = (self.roi2 * np.array([self.width, self.height])).astype("int64")
        self.roi_3 = (self.roi3 * np.array([self.width, self.height])).astype("int64")

        self.roi_1 = Polygon(self.roi_1)
        self.roi_2 = Polygon(self.roi_2)
        self.roi_3 = Polygon(self.roi_3)

        self.coords1 = np.array([[*self.roi_1.exterior.coords]]).astype("int64")
        self.coords2 = np.array([[*self.roi_2.exterior.coords]]).astype("int64")
        self.coords3 = np.array([[*self.roi_3.exterior.coords]]).astype("int64")

        image = cv2.polylines(
            image,
            self.coords1,
            isClosed=True,
            color=[255, 0, 0],
            thickness=3,
        )
        image = cv2.polylines(
            image,
            self.coords2,
            isClosed=True,
            color=[255, 0, 0],
            thickness=3,
        )
        image = cv2.polylines(
            image,
            self.coords3,
            isClosed=True,
            color=[255, 0, 0],
            thickness=3,
        )
        triler_dic = trailer_manager(self.i)
        values = triler_dic.Values_trai()
        # print(values.keys())
        while True:
            
            for i, key in enumerate(values):
                image_drow = image
                x1, y1, x2, y2 = values[f"{key}"][:4]
                x1 = int(x1) * self.width // 10000
                y1 = int(y1) * self.height // 10000
                x2 = int(x2) * self.width // 10000
                y2 = int(y2) * self.height // 10000
                id=values[f"{key}"][5]
                image_drow1 = cv2.putText(
                    image_drow,
                    str(id),
                    # str(key),
                    (x1, y1-25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 0, 255),
                    15,
                    cv2.LINE_AA,
                )
                image_drow2 = cv2.rectangle(image_drow1, (x1, y1), (x2, y2), (0, 255, 0), 2)
    

                if self.write_queue.empty():
                    self.write_queue.put(image_drow2)

                # time.sleep(1)

                # print(self.url)
                # if len(self.dic_img) <= 4:
                #     for z in self.url:
                #         self.dic_img[self.url]=image_drow2

                # # display=display(self.dic_img)
                # # display.run()

                # print("end")
                # self.dic_img={}

                # print(self.dic_img)

            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            # cv2.namedWindow(f"{self.data}1", cv2.WINDOW_NORMAL)
            print("hello")

            # cv2.imshow(f"{self.data}", image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            # print("completed hello")
            # print(self.url)
