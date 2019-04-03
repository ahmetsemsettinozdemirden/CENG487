# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from scene import Scene
from factory.objectparser import ObjectParser
from factory.camerafactory import CameraFactory
from linear.mat3d import Mat3D

class MainScene(Scene):

    def __init__(self):
        super(MainScene, self).__init__()
        self.cameraFactory = CameraFactory()
        self.objectParser = ObjectParser()
        self.subdivisionLevel = 1

    def init(self, objDest):
        self.mainCamera = self.cameraFactory.create(0.0, 0.0, -10.0)
        self.obj = self.objectParser.create(objDest)
        self.objDest = objDest

    def keyPressed(self, key):
        # TODO: subdivision
        if key == '+' and self.subdivisionLevel < 10:
            self.subdivisionLevel += 1
            self.subdivide(self.subdivisionLevel)
        elif key == '-' and self.subdivisionLevel > 1:
            self.subdivisionLevel -= 1
            self.subdivide(self.subdivisionLevel)
        elif key == 'LEFT_ARROW':
            self.obj.transform.rotateY(5.0)
        elif key == 'RIGHT_ARROW':
            self.obj.transform.rotateY(-5.0)
        elif key == 'UP_ARROW':
            self.obj.transform.rotateX(5.0)
        elif key == 'DOWN_ARROW':
            self.obj.transform.rotateX(-5.0)
        elif key == 'r':
            self.obj.transform.reset()

    def update(self):
        # self.obj.transform.rotateX(1)
        # self.mainCamera.transform.rotateX(1)
        pass

    def render(self):
        self.obj.draw(self.mainCamera)

    def subdivide(self, subdivisionLevel):
        self.obj = self.objectParser.create(self.objDest)
        # start from level 2 since level 1 subdivision is equal to object itself.
        for i in range(subdivisionLevel - 1):
            self.obj.subdivide()