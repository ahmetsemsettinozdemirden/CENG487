# CENG 487 Assignment1 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019

from vec3d import Vec3d
import math

class Mat3d:

    def __init__(self, matrix):
        self.matrix = matrix

    def multiply(self, vec3d):
        return Vec3d(
            self.matrix[0].dotProduct(vec3d), 
            self.matrix[1].dotProduct(vec3d), 
            self.matrix[2].dotProduct(vec3d), 
            self.matrix[3].dotProduct(vec3d))

    def transpose():
        return [Vec3d(self.matrix[0].x, self.matrix[1].x, self.matrix[2].x, self.matrix[3].x),
                Vec3d(self.matrix[0].y, self.matrix[1].y, self.matrix[2].y, self.matrix[3].y),
                Vec3d(self.matrix[0].z, self.matrix[1].z, self.matrix[2].z, self.matrix[3].z),
                Vec3d(self.matrix[0].w, self.matrix[1].w, self.matrix[2].w, self.matrix[3].w)]
        
    @staticmethod
    def translationMatrix(x, y, z):
        return Mat3d([  Vec3d(1, 0, 0, x),
                        Vec3d(0, 1, 0, y),
                        Vec3d(0, 0, 1, z),
                        Vec3d(0, 0, 0, 1)])

    @staticmethod
    def scalingMatrix(x, y, z):
        return Mat3d([  Vec3d(x, 0, 0, 0),
                        Vec3d(0, y, 0, 0),
                        Vec3d(0, 0, z, 0),
                        Vec3d(0, 0, 0, 1)])

    @staticmethod
    def rotationXMatrix(ang):
        return Mat3d([  Vec3d(1, 0,             0,              0),
                        Vec3d(0, math.cos(ang), -math.sin(ang), 0),
                        Vec3d(0, math.sin(ang), math.cos(ang),  0),
                        Vec3d(0, 0,             0,              1)])

    @staticmethod
    def rotationYMatrix(ang):
        return Mat3d([  Vec3d(math.cos(ang),  0, math.sin(ang), 0),
                        Vec3d(0,              1, 0,             0),
                        Vec3d(-math.sin(ang), 0, math.cos(ang), 0),
                        Vec3d(0,              0, 0,             1)])

    @staticmethod
    def rotationZMatrix(ang):
        return Mat3d([  Vec3d(math.cos(ang), -math.sin(ang), 0, 0),
                        Vec3d(math.sin(ang), math.cos(ang),  0, 0),
                        Vec3d(0,             0,              1, 0),
                        Vec3d(0,             0,              0, 1)])

    @staticmethod
    def sheerMatrix(x, y, z):
        TODO