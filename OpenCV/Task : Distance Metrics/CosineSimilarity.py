import numpy as np
import logging
logger = logging.getLogger("distance finder")


class CosineSimilarity:
    def __init__(self, first_point, second_point) -> None:
        self.first_point = first_point
        self.second_point = second_point
        if self.first_point is None or self.second_point is None:
            logger.critical(f"points values is None")
        else:
            self.find_distance()

    def find_distance(self):
        first_magnitude = np.linalg.norm(self.first_point)
        second_magnitude = np.linalg.norm(self.second_point)
        if first_magnitude==0:
            first_magnitude==0.001
        if second_magnitude==0.0:
            second_magnitude=0.001
        try: 
            cosine_similarity = np.dot(self.first_point, self.second_point) / (first_magnitude * second_magnitude)
        except:
            logger.info(f"points values is near zero")
        cosine_distance = 1 - cosine_similarity
        print(f"Cosine Distance is {cosine_distance}")
