import numpy as np
import math
from EuclideanDistance import *
import logging
logger = logging.getLogger("distance finder")

class PolarDistance:
    def __init__(self,first_point,second_point) -> None:
        self.first_point = first_point
        self.second_point = second_point
        
        
        if self.first_point is None or self.second_point is None:
            logger.critical(f"points values is None")
        else:
            first_line_angle=self.find_angle(self.first_point)
            second_line_angle=self.find_angle(self.second_point)
            self.two_points_theta=abs(first_line_angle-second_line_angle*math.pi / 180)
            self.find_distance()
        
    def find_angle(self,points):
        self.point=points
        if self.point[0]==0:
            theta_value=np.inf
        else:
            theta_value=self.point[1]/self.point[0]
        self.theta=(math.atan(theta_value)*180/math.pi)
        return self.theta
        
        
    def find_distance(self):
        first_length_object=EuclideanDistance(self.first_point, np.array([0,0]))
        second_length_object=EuclideanDistance(self.second_point, np.array([0,0]))
        first_length=first_length_object.find_distance()
        second_length=second_length_object.find_distance()
        # print(first_length,second_length,self.two_points_theta,math.cos(self.two_points_theta))
        polar_distance = math.sqrt(first_length**2+second_length**2-(2*first_length*second_length*math.cos(self.two_points_theta)))
        print(f'Polar Distance  is {polar_distance}')
