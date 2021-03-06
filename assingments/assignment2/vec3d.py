# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
import math

class Vec3d(object):
    
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "Vec3d [x:" + str(self.x) + ", y:" + str(self.y) + ", z:" + str(self.z) + ", w:" + str(self.w) + "]" 

    # vector arithmetic methods
    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def scale(self, n):
        self.x *= n
        self.y *= n
        self.z *= n

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # vector and point manipulation operations
    def dotProduct(self, vec3d):
        return self.x * vec3d.x + self.y * vec3d.y + self.z * vec3d.z

    def crossProduct(self, vec3d):
        return vec3d(
            self.y * vec3d.z + self.z * vec3d.y, 
            self.z * vec3d.x + self.x * vec3d.z, 
            self.x * vec3d.y + self.y * vec3d.x,
            1.0)

    def angle(self, vec3d):
        return math.acos(self.dotProduct(vec3d) / (self.magnitude() * vec3d.magnitude()))
        
    # unit vectors
    @staticmethod
    def vec_i():
        return Vec3d(1,0,0,0)
        
    @staticmethod
    def vec_j():
        return Vec3d(0,1,0,0)
        
    @staticmethod
    def vec_k():
        return Vec3d(0,0,1,0)

    @staticmethod
    def vec_w():
        return Vec3d(0,0,0,1)
        
