"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distance_from_xy(self, x, y):
        return math.sqrt((self.y-y)**2+(self.x-x)**2)

    def distance_from_point(self, point):
        return math.sqrt((self.y-point.y)**2+(self.x-point.x)**2)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.a = vertice1
        self.b = vertice2
        self.c = vertice3
    def perimeter(self):
        return (
            self.a.distance_from_point(self.b) + 
            self.b.distance_from_point(self.c) + 
            self.a.distance_from_point(self.c)
        )
        


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())