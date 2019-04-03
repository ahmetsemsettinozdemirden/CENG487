# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from linear.vec3d import Vec3D
from model.model3d import Model3D
from model.face3d import Face3D
from transform import Transform

class ObjectParser(object):

    def create(self, objDest):
        vertices = []
        faces = []

        # read file and get rid of '\n' at the end of each line.
        with open(objDest) as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines] 

        # parse vertices
        for line in lines:
            if line != '' and line[0] is 'v':
                vertexLine = line.split(' ')
                # create vertex
                vertices.append(Vec3D(float(vertexLine[1]), 
                                      float(vertexLine[2]),
                                      float(vertexLine[3]),
                                      1.0))
        
        # parse faces
        for line in lines:
            if line != '' and line[0] is 'f':
                # find vertex indices
                faceElements = [int(e) for e in line.split(' ')[1:]]
                faceVertices = []
                for faceElement in faceElements:
                    faceVertices.append(vertices[faceElement - 1].clone())
                # create face with color
                faces.append(Face3D(faceVertices, [0.6, 0.6, 0.8]))

        # create object with faces
        return Model3D(Transform(Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(0.0, 0.0, 0.0, 1.0), Vec3D(1.0, 1.0, 1.0, 1.0)), faces)
