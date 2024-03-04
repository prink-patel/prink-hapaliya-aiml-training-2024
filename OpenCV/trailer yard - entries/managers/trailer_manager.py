import json
import cv2

class trailer_manager:

    def __init__(self, img_copy, data, frame_id):
        self.frame_id = frame_id
        self.img_copy = img_copy
        self.data = data

    def run(self):

        for idy in range(len(self.data["messages"][self.frame_id]["objects"])):

            if (
                self.data["messages"][self.frame_id]["objects"][idy].split("|")[0]
                == "TOP"
            ):

                object_data = self.data["messages"][self.frame_id]["objects"][
                    idy
                ].split("|")
                trailer_id = object_data[1]
                x1 = object_data[3]
                y1 = object_data[4]
                x2 = object_data[5]
                y2 = object_data[6]

                height, width = self.img_copy.shape[:2]

                x1 = int(x1) * width // 10000
                x2 = int(x2) * width // 10000
                y1 = int(y1) * height // 10000
                y2 = int(y2) * height // 10000
                center=(x2 + x1)//2, (y2+y1)//2
                

                self.img_copy1 = cv2.circle(self.img_copy, center , 10, (0, 0, 255) , -1) 
                
                self.img_copy2 = cv2.rectangle(self.img_copy1, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(
                    self.img_copy2,
                    trailer_id,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0, 255, 0),
                    10,
                )
        return self.img_copy2
