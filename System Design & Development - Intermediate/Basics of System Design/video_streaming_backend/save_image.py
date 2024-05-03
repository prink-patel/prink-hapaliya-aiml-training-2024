import base64
import cv2
import numpy as np
import uuid
import os
import logging
logger = logging.getLogger("Streaming_data")


class SaveImage:
    def __init__(self) -> None:
        logger.info("Image saved object create")
        self.count = 0

    #decode image from base64
    def run(self, img_str):
        try:
            logger.info("Image saved run method started")
            self.img_str = img_str
            decode_image = base64.b64decode(self.img_str)
            matrix_image = np.frombuffer(decode_image, np.uint8)
            self.image = cv2.imdecode(matrix_image, cv2.IMREAD_COLOR)
            return self.save_image()
        except Exception as e:
            logger.critical("image not valid formate or not found")

    # save image
    def save_image(self):
        logger.info("Image saved")
        img_path = os.path.join(r"demo", r"images", f"{self.count}_{str(uuid.uuid1())}.jpg")
        self.count = self.count + 1
        cv2.imwrite(img_path, self.image)
        return img_path
