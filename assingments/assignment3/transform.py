# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from linear.vec3d import Vec3D
from linear.mat3d import Mat3D

# This class basically defines a space. Since any object (e.g. camera) can use this class, 
# naming as 'Transform' is better then 'Space'. The code is self explanatory.
class Transform(object):

    def __init__(self, position, rotation, scaler):
        self.position = position
        self.rotation = rotation
        self.scaler = scaler
        self.finalMatrix = Mat3D.identityMatrix()

    def __str__(self):
        return "Transform, position: [x:" + str(self.position.x) + ", y:" + str(self.position.y) + ", z:" + str(self.position.z) + "], rotation: [x:" + str(self.rotation.x) + ", y:" + str(self.rotation.y) + ", z:" + str(self.rotation.z) + "], scale: [x:" + str(self.scaler.x) + ", y:" + str(self.scaler.y) + ", z:" + str(self.scaler.z) + "]" 

    def setPosition(self, x, y, z):
        self.position = Vec3D(x, y, z, 1.0)

    def setRotation(self, x, y, z):
        self.rotation = Vec3D(x, y, z, 1.0)

    def setScaler(self, x, y, z):
        self.scaler = Vec3D(x, y, z, 1.0)

    def translate(self, x, y, z):
        self.position.add(Vec3D(x, y, z, 1.0))
        self.applyTransformationMatrix(Mat3D.translationMatrix(x, y, z))

    def rotateX(self, ang):
        self.rotation.x += ang
        self.applyTransformationMatrix(Mat3D.rotationXMatrix(ang))

    def rotateY(self, ang):
        self.rotation.y += ang
        self.applyTransformationMatrix(Mat3D.rotationYMatrix(ang))

    def rotateZ(self, ang):
        self.rotation.z += ang
        self.applyTransformationMatrix(Mat3D.rotationZMatrix(ang))

    def scale(self, x, y, z):
        self.scaler.add(Vec3D(x, y, z, 1.0))
        self.applyTransformationMatrix(Mat3D.scalingMatrix(x, y, z))

    def reset(self):
        self.position = Vec3D(0.0, 0.0, 0.0, 1.0)
        self.rotation = Vec3D(0.0, 0.0, 0.0, 1.0)
        self.scaler = Vec3D(1.0, 1.0, 1.0, 1.0)
        self.finalMatrix = Mat3D.identityMatrix()

    def applyTransformationMatrix(self, matrix):
        self.finalMatrix = self.finalMatrix.multiplyMatrix(matrix)
