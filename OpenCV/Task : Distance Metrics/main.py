import numpy as np

# from camera import *
from CosineSimilarity import *
from ManhattanDistance import *
from PolarDistance import *
from EuclideanDistance import *
import logging
import cv2

logging.basicConfig(
    filename="logging_file.log",
    format="%(levelname)s - %(asctime)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger("distance finder")
logger.setLevel(logging.INFO)


class camera:
    def __init__(self):
        self.img = cv2.imread("/home/wot-prink/Downloads/1187763.jpg", 1)
        self.img = cv2.resize(self.img, (1200, 700))
        self.right_point_list = None
        self.left_point_list = None
        count_ = 0
        # displaying the image
        cv2.imshow("image", self.img)

        # setting mouse handler for the image
        # and calling the click_event() function

        click_event = self.click_event
        cv2.setMouseCallback("image", click_event)
        # wait for a key to be pressed to exit

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def click_event(self, event, x, y, flags, params):

        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:

            # displaying the coordinates
            # on the Shell
            print(x, " ", y)
            self.left_point_list = np.array([x, y])

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                self.img, str(x) + "," + str(y), (x, y), font, 1, (255, 0, 0), 2
            )
            cv2.imshow("image", self.img)

        # checking for right mouse clicks
        if event == cv2.EVENT_RBUTTONDOWN:

            print(x, " ", y)
            self.right_point_list = np.array([x, y])

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                self.img, str(x) + "," + str(y), (x, y), font, 1, (255, 0, 0), 2
            )

            image = cv2.line(
                self.img,
                self.left_point_list,
                self.right_point_list,
                (0, 255, 0),
                5,
            )

            cv2.imshow("image", self.img)
            print(self.right_point_list, self.left_point_list)
            CosineSimilarity(self.right_point_list, self.left_point_list)
            ManhattanDistance(self.right_point_list, self.left_point_list)
            PolarDistance(self.right_point_list, self.left_point_list)
            euclidean_distance_object = EuclideanDistance(
                self.right_point_list, self.left_point_list
            )
            euclidean_distance = euclidean_distance_object.find_distance()
            logger.info(f"Euclidean Distance  is {euclidean_distance}")
            logger.info(f"----------------------------------------------")


# first_point = np.array([4, 0])
# second_point = np.array([0, 0])
camera()
