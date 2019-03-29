# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from scene import Scene
from factory.boxfactory import BoxFactory
from factory.spherefactory import SphereFactory
from mat3d import Mat3d

class MainScene(Scene):

    def __init__(self, camera):
        super(MainScene, self).__init__(camera)
        self.subdivisionCount = 1
        self.boxFactory = BoxFactory()
        self.sphereFactory = SphereFactory()

    def init(self):
        # self.box = self.boxFactory.create()
        self.sphere = self.sphereFactory.create()

    def keyPressed(self, *args):
        if args[0] == '+' and self.subdivisionCount < 10:
            self.subdivisionCount += 1
        elif args[0] == '-' and self.subdivisionCount > 1:
            self.subdivisionCount -= 1
        # self.box = self.boxFactory.create(subdivisionCount=self.subdivisionCount)
        self.sphere = self.sphereFactory.create(sectorCount=5+self.subdivisionCount, stackCount=5+self.subdivisionCount)

    def update(self):
        # self.box.update()
        # self.box.transform.rotation.x += 0.02
        # self.box.transform.rotation.y += 0.02
        # self.box.transform.rotation.z += 0.02
        self.sphere.update()
        self.sphere.transform.rotation.x += 0.02

    def render(self):
	    # self.box.draw()
        self.sphere.draw()
