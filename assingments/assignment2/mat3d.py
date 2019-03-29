# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019

from vec3d import Vec3d
import math

class Mat3d(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def multiplyVector(self, vec3d):
        return Vec3d(self.matrix[0][0] * vec3d.x + self.matrix[0][1] * vec3d.y + self.matrix[0][2] * vec3d.z + self.matrix[0][3] * vec3d.w,
                     self.matrix[1][0] * vec3d.x + self.matrix[1][1] * vec3d.y + self.matrix[1][2] * vec3d.z + self.matrix[1][3] * vec3d.w, 
                     self.matrix[2][0] * vec3d.x + self.matrix[2][1] * vec3d.y + self.matrix[2][2] * vec3d.z + self.matrix[2][3] * vec3d.w, 
                     1.0)
    
    def multiplyMatrix(self, mat3d):
        return Mat3d([[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*mat3d.matrix)] for X_row in self.matrix])

    def transpose(self):
        return Mat3d([[self.matrix[0][0], self.matrix[1][0], self.matrix[2][0], self.matrix[3][0]],
                      [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1], self.matrix[3][1]],
                      [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2], self.matrix[3][2]],
                      [self.matrix[0][3], self.matrix[1][3], self.matrix[2][3], self.matrix[3][3]]])
        
    @staticmethod
    def identityMatrix():
        return Mat3d([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def translationMatrix(x, y, z):
        return Mat3d([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])

    @staticmethod
    def scalingMatrix(x, y, z):
        return Mat3d([[x, 0, 0, 0],
                      [0, y, 0, 0],
                      [0, 0, z, 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def rotationXMatrix(ang):
        return Mat3d([[1, 0,             0,              0],
                      [0, math.cos(ang), -math.sin(ang), 0],
                      [0, math.sin(ang), math.cos(ang),  0],
                      [0, 0,             0,              1]])

    @staticmethod
    def rotationYMatrix(ang):
        return Mat3d([[math.cos(ang),  0, math.sin(ang), 0],
                      [0,              1, 0,             0],
                      [-math.sin(ang), 0, math.cos(ang), 0],
                      [0,              0, 0,             1]])

    @staticmethod
    def rotationZMatrix(ang):
        return Mat3d([[math.cos(ang), -math.sin(ang), 0, 0],
                      [math.sin(ang), math.cos(ang),  0, 0],
                      [0,             0,              1, 0],
                      [0,             0,              0, 1]])

    @staticmethod
    def sheerMatrix(xy, yx, xz, zx, yz, zy):
        return Mat3d([[ 1, xy, xz, 0],
                      [yx,  1, yz, 0],
                      [zx, zy,  1, 0],
                      [ 0,  0,  0, 1]])