# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from vec3d import Vec3d
from transform import Transform
from model3d import Model3D

class BoxFactory(object):

    def create(self, subdivisionCount = 1):

        vertices = [
            Vec3d( 1.0, -1.0, -1.0, 1.0),
            Vec3d( 1.0, -1.0,  1.0, 1.0),
            Vec3d(-1.0, -1.0,  1.0, 1.0),
            Vec3d(-1.0, -1.0, -1.0, 1.0),
            Vec3d( 1.0,  1.0, -1.0, 1.0),
            Vec3d( 1.0,  1.0,  1.0, 1.0),
            Vec3d(-1.0,  1.0,  1.0, 1.0),
            Vec3d(-1.0,  1.0, -1.0, 1.0)]

        faces = [
            [1, 2, 3, 4],
            [5, 8, 7, 6],
            [1, 5, 6, 2],
            [2, 6, 7, 3],
            [3, 7, 8, 4],
            [5, 1, 4, 8]]

        faceColors = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0]]

        return Model3D(Transform(), vertices, faces, faceColors)