# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from vec3d import Vec3d
from transform import Transform
from camera import Camera

class CameraFactory(object):

    def create(self, x, y, z):
        return Camera(Transform(Vec3d(x, y, z, 1)))