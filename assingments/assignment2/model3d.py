# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from OpenGL.GL import *

class Model3D(object):

    def __init__(self, transform, vertices, faces, faceColors):
        self.transform = transform
        self.vertices = vertices
        self.faces = faces
        self.faceColors = faceColors

    def update(self):
        self.transform.update()

    def draw(self):
        verticesPos = [ self.transform.finalMatrix.multiplyVector(vertex) for vertex in self.vertices ]
        for faceIndex, face in enumerate(self.faces):
            glBegin(GL_POLYGON)
            color = self.faceColors[faceIndex]
            glColor3f(color[0], color[1], color[2])
            for vertexIndex in face:
                vertex = verticesPos[vertexIndex-1]
                glVertex3f(vertex.x, vertex.y, vertex.z)
    	    glEnd()