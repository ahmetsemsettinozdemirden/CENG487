# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from vec3d import Vec3d
from mat3d import Mat3d

# This class basically defines a space. Since objects like camera can use this object, naming as 'Transform' is better then 'Space'.
class Transform(object):

    def __init__(self, position = Vec3d(0.0, 0.0, 0.0, 1.0),
                rotation = Vec3d(0.0, 0.0, 0.0, 1.0),
                scaler = Vec3d(1.0, 1.0, 1.0, 1.0)):
        self.position = position
        self.rotation = rotation
        self.scaler = scaler
        self.matrixStack = []
        self.finalMatrix = Mat3d.identityMatrix()

    def __str__(self):
        return "Transform, position: [x:" + str(self.position.x) + ", y:" + str(self.position.y) + ", z:" + str(self.position.z) + "], rotation: [x:" + str(self.rotation.x) + ", y:" + str(self.rotation.y) + ", z:" + str(self.rotation.z) + "], scale: [x:" + str(self.scaler.x) + ", y:" + str(self.scaler.y) + ", z:" + str(self.scaler.z) + "]" 

    def setPosition(self, x, y, z):
        self.position = Vec3d(x, y, z, 1.0)

    def setRotation(self, x, y, z):
        self.rotation = Vec3d(x, y, z, 1.0)

    def setScaler(self, x, y, z):
        self.scaler = Vec3d(x, y, z, 1.0)

    def translate(self, x, y, z):
        self.addTransformationMatrix(Mat3d.translationMatrix(x, y, z))

    def rotateX(self, ang):
        self.addTransformationMatrix(Mat3d.rotationXMatrix(ang))

    def rotateY(self, ang):
        self.addTransformationMatrix(Mat3d.rotationYMatrix(ang))

    def rotateZ(self, ang):
        self.addTransformationMatrix(Mat3d.rotationZMatrix(ang))

    def scale(self, x, y, z):
        self.addTransformationMatrix(Mat3d.scalingMatrix(x, y, z))

    def addTransformationMatrix(self, matrix):
        self.matrixStack.append(matrix)
        self.finalMatrix = self.finalMatrix.multiplyMatrix(matrix)

    def update(self):
        # reset matrix stack
        self.matrixStack = []
        self.finalMatrix = Mat3d.identityMatrix()
        # calculate final matrix
        self.translate(self.position.x, self.position.y, self.position.z)
        self.rotateX(self.rotation.x)
        self.rotateY(self.rotation.y)
        self.rotateZ(self.rotation.z)
        self.scale(self.scaler.x, self.scaler.y, self.scaler.z)
