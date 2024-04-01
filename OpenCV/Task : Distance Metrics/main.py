import numpy as np
from camera import *
from CosineSimilarity import *
from ManhattanDistance import *
from PolarDistance import *
from EuclideanDistance import *
import logging

logging.basicConfig(
    filename="logging_file.log",
    format="%(levelname)s - %(asctime)s - %(message)s",
    filemode="w",
)
logger = logging.getLogger("distance finder")
logger.setLevel(logging.INFO)


# first_point = np.array([4, 0])
# second_point = np.array([0, 0])

first_point,second_point=camera()
CosineSimilarity(first_point, second_point)
ManhattanDistance(first_point, second_point)
PolarDistance(first_point, second_point)
euclidean_distance_object=EuclideanDistance(first_point, second_point)
euclidean_distance=euclidean_distance_object.find_distance()

print(f'Euclidean Distance  is {euclidean_distance}')