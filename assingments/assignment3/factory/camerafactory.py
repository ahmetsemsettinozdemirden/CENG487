# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from linear.vec3d import Vec3D
from transform import Transform
from camera import Camera

class CameraFactory(object):

    def create(self, x, y, z):
        # creates and translates the camera
        camera = Camera(Transform(Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(1.0, 1.0, 1.0, 1.0)))
        camera.transform.translate(x, y, z)
        return camera