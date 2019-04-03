# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
import math
from linear.vec3d import Vec3D
from model.model3d import Model3D
from transform import Transform

# References:
# http://www.songho.ca/opengl/gl_sphere.html

class SphereFactory(object):

    def create(self, radius = 1.0, sectorCount = 12, stackCount = 12):

        # generate vertices
        vertices = []

        sectorStep = 2 * math.pi / sectorCount
        stackStep = math.pi / stackCount

        for i in range(stackCount + 1):

            stackAngle = math.pi / 2 - i * stackStep
            xy = radius * math.cos(stackAngle)
            z = radius * math.sin(stackAngle)

            for j in range(sectorCount + 1):

                sectorAngle = j * sectorStep

                x = xy * math.cos(sectorAngle)
                y = xy * math.sin(sectorAngle)

                vertices.append(Vec3D(x, y, z, 1.0))
        
        # generate faces
        faces = []
        for i in range(stackCount):
            
            k1 = i * (sectorCount + 1)
            k2 = k1 + sectorCount + 1

            for j in range(sectorCount + 1):

                if i != 0:
                    faces.append([k1, k2, k1 + 1])

                if i != (stackCount - 1):
                    faces.append([k1 + 1, k2, k2 + 1])

                k1 += 1
                k2 += 1

        # generate face colors
        faceColors = []
        for i in range(len(faces)):
            faceColors.append([0.8, 0.8, 1.0])

        return Model3D(Transform(Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(1.0, 1.0, 1.0, 1.0)), faces)





        