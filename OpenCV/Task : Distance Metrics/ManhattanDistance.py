import numpy as np
import logging

logger = logging.getLogger("distance finder")


class ManhattanDistance:
    def __init__(self, first_point, second_point) -> None:

        self.first_point = first_point
        self.second_point = second_point
        if self.first_point is None or self.second_point is None:
            logger.critical(f"points values is None")
        else:
            self.find_distance()

    def find_distance(self):
        manhattan_distance = sum(
            abs(val1 - val2) for val1, val2 in zip(self.first_point, self.second_point)
        )
        logger.info(f"Manhattan Distance  is {manhattan_distance}")
