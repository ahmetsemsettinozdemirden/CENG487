# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from linear.vec3d import Vec3D
from model.model3d import Model3D
from transform import Transform

class ObjectParser(object):

    def create(self, objDest):
        vertices = []
        faces = []
        faceColors = []

        with open(objDest) as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines] 

        # while reading the faces we assume that all vertices are defined before faces
        for line in lines:
            if line != '':
                if line[0] is 'v':
                    vertexLine = line.split(' ')
                    vertices.append(Vec3D(float(vertexLine[1]), 
                                          float(vertexLine[2]),
                                          float(vertexLine[3]),
                                          1.0))
                elif line[0] is 'f':
                    faceElements = [int(e) for e in line.split(' ')[1:]]
                    faces.append(faceElements)
                    faceColors.append([0.6, 0.6, 0.8])

        return Model3D(Transform(Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(1.0, 1.0, 1.0, 1.0)), vertices, faces, faceColors)
