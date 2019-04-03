# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
import math
from linear.vec3d import Vec3D

class Mat3D(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def multiplyVector(self, vec3d):
        return Vec3D(self.matrix[0][0] * vec3d.x + self.matrix[0][1] * vec3d.y + self.matrix[0][2] * vec3d.z + self.matrix[0][3] * vec3d.w,
                     self.matrix[1][0] * vec3d.x + self.matrix[1][1] * vec3d.y + self.matrix[1][2] * vec3d.z + self.matrix[1][3] * vec3d.w, 
                     self.matrix[2][0] * vec3d.x + self.matrix[2][1] * vec3d.y + self.matrix[2][2] * vec3d.z + self.matrix[2][3] * vec3d.w, 
                     1.0)
    
    def multiplyMatrix(self, mat3d):
        return Mat3D([[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*mat3d.matrix)] for X_row in self.matrix])

    def transpose(self):
        return Mat3D([[self.matrix[0][0], self.matrix[1][0], self.matrix[2][0], self.matrix[3][0]],
                      [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1], self.matrix[3][1]],
                      [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2], self.matrix[3][2]],
                      [self.matrix[0][3], self.matrix[1][3], self.matrix[2][3], self.matrix[3][3]]])
        
    @staticmethod
    def identityMatrix():
        return Mat3D([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def translationMatrix(x, y, z):
        return Mat3D([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])

    @staticmethod
    def scalingMatrix(x, y, z):
        return Mat3D([[x, 0, 0, 0],
                      [0, y, 0, 0],
                      [0, 0, z, 0],
                      [0, 0, 0, 1]])

    @staticmethod
    def rotationXMatrix(deg):
        rad = math.radians(deg)
        return Mat3D([[1, 0,             0,              0],
                      [0, math.cos(rad), -math.sin(rad), 0],
                      [0, math.sin(rad), math.cos(rad),  0],
                      [0, 0,             0,              1]])

    @staticmethod
    def rotationYMatrix(deg):
        rad = math.radians(deg)
        return Mat3D([[math.cos(rad),  0, math.sin(rad), 0],
                      [0,              1, 0,             0],
                      [-math.sin(rad), 0, math.cos(rad), 0],
                      [0,              0, 0,             1]])

    @staticmethod
    def rotationZMatrix(deg):
        rad = math.radians(deg)
        return Mat3D([[math.cos(rad), -math.sin(rad), 0, 0],
                      [math.sin(rad), math.cos(rad),  0, 0],
                      [0,             0,              1, 0],
                      [0,             0,              0, 1]])

    @staticmethod
    def sheerMatrix(xy, yx, xz, zx, yz, zy):
        return Mat3D([[ 1, xy, xz, 0],
                      [yx,  1, yz, 0],
                      [zx, zy,  1, 0],
                      [ 0,  0,  0, 1]])