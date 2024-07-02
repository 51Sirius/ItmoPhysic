import math
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import affinity



class VariableCapacitor:
    def __init__(self, angle_speed, d, width, length, e):
        self.d = d / 1000
        self.angle_speed = angle_speed
        self.width = width / 100
        self.length = length / 100
        self.e = e

    def get_pool(self, t):
        print(self.get_area(t) * self.e / self.d + (
                self.width * self.length - self.get_area(t)) / self.d)
        return self.get_area(t) * self.e * (8.854 * 10 ** (-12)) / self.d + (
                self.width * self.length - self.get_area(t)) * (8.854 * 10 ** (-12)) / self.d

    def get_area(self, t):
        rectangle1 = Polygon([(0, 0), (self.length, 0), (self.length, self.width), (0, self.width)])

        rectangle2 = Polygon([(0, 0), (self.length, 0), (self.length, self.width), (0, self.width)])
        rectangle2 = affinity.rotate(rectangle2, self.angle_speed * t)

        intersection = rectangle1.intersection(rectangle2)

        intersection_area = intersection.area

        return intersection_area

    def get_plot(self, t):
        arr = []
        for t1 in t:
            arr.append(self.get_pool(t1))
        return arr
