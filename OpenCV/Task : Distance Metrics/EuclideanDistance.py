import numpy as np
import logging
logger = logging.getLogger("distance finder")

class EuclideanDistance:
    def __init__(self,first_point,second_point) :
        self.first_point=first_point
        self.second_point=second_point
        
    def find_distance(self):
        if self.first_point is None or self.second_point is None:
            logger.critical(f"points values is None")
        else:
            return np.sqrt(np.sum(np.square(self.first_point-self.second_point)))
       