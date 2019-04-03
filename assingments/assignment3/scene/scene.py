# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from factory.camerafactory import CameraFactory
from factory.objectparser import ObjectParser
from factory.spherefactory import SphereFactory

class Scene(object):

    def __init__(self):
        self.cameraFactory = CameraFactory()
        self.objectParser = ObjectParser()
        self.sphereFactory = SphereFactory()

    def init(self):
        print("no init implementation")

    def keyPressed(self, *args):
        print("no keyPressed implementation")

    def update(self):
        print("no update implementation")

    def render(self):
        print("no render implementation")

    def createCamera(self, x, y, z):
        return self.cameraFactory.create(x, y, z)

    def createObject(self, dest):
        return self.objectParser.create(dest)

    def createSphere(self, radius = 1.0, sectorCount = 12, stackCount = 12):
        return self.sphereFactory.create(radius, sectorCount, stackCount)