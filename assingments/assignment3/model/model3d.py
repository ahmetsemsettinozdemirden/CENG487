# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from OpenGL.GL import *
from linear.vec3d import Vec3D

class Model3D(object):

    def __init__(self, transform, vertices, faces, faceColors):
        self.transform = transform
        self.vertices = vertices
        self.faces = faces
        self.faceColors = faceColors

    def draw(self, camera):
        # calculate final matrix from camera and model position
        finalMatrix = camera.transform.finalMatrix.multiplyMatrix(self.transform.finalMatrix)
        # calculate vertex matrices by using final matrix
        verticesPos = [finalMatrix.multiplyVector(vertex) for vertex in self.vertices]
        # draw shape
        for faceIndex, face in enumerate(self.faces):
            # draw polygonal face
            glBegin(GL_POLYGON)
            color = self.faceColors[faceIndex]
            glColor3f(color[0], color[1], color[2])
            for vertexIndex in face:
                vertex = verticesPos[vertexIndex-1]
                glVertex3f(vertex.x, vertex.y, vertex.z)
    	    glEnd()
            # draw edges
            glLineWidth(2.5)
            glBegin(GL_LINE_STRIP)
            glColor3f(.3, .3, .3)
            for vertexIndex in face:
                vertex = verticesPos[vertexIndex-1]
                glVertex3f(vertex.x, vertex.y, vertex.z)
    	    glEnd()

    def subdivide(self):
        # TODO: For each face calculate a point at the center of the face
        # TODO: For each edge calculate a mid point between its vertices.
        # TODO: Then connect each of those mid points to the center point of the face, to create 4 polygons (quads) per face.

        newVertices = []
        newFaces = []

        for faceIndex, face in enumerate(self.faces):

            # calculate center of faces
            centerOfFace = Vec3D(0.0, 0.0, 0.0, 1.0)
            for vertexIndex in face:
                vertex = self.vertices[vertexIndex-1]
                centerOfFace.add(vertex)
            centerOfFace.scale(1.0/len(face))

            # calculate midpoints for each edge
            midPoints = []
            for vertexIndex in face:
                vertex1 = self.vertices[vertexIndex-1]
                vertex2 = self.vertices[0 if vertexIndex >= len(face) else vertexIndex]
                midPoint = vertex1.clone()
                midPoint.add(vertex2)
                midPoint.scale(0.5)
                midPoints.append(midPoint)

                
                
            print(centerOfFace)
            print(midPoints)

    