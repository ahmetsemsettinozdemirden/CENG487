# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from OpenGL.GL import *
from linear.vec3d import Vec3D
from model.face3d import Face3D

class Model3D(object):

    def __init__(self, transform, faces):
        self.transform = transform
        self.faces = faces

    def draw(self, camera):
        # calculate final matrix from camera and model position
        finalMatrix = camera.transform.finalMatrix.multiplyMatrix(self.transform.finalMatrix)
        # draw shape
        for face in self.faces:
            # calculate vertex matrices by using final matrix
            verticesPos = [finalMatrix.multiplyVector(vertex) for vertex in face.vertices]
            # draw polygonal face
            glBegin(GL_POLYGON)
            glColor3f(face.color[0], face.color[1], face.color[2])
            for vertex in verticesPos:
                glVertex3f(vertex.x, vertex.y, vertex.z)
    	    glEnd()
            # draw edges
            glLineWidth(2.5)
            glBegin(GL_LINE_LOOP)
            glColor3f(.3, .3, .3)
            for vertex in verticesPos:
                glVertex3f(vertex.x, vertex.y, vertex.z)
    	    glEnd()

    def subdivide(self):
        newFaces = []
        for face in self.faces:
            
            # calculate center of faces
            centerOfFace = Vec3D(0.0, 0.0, 0.0, 1.0)
            for vertex in face.vertices:
                centerOfFace.add(vertex)
            centerOfFace.scale(1.0/len(face.vertices))

            # calculate midpoints for each edge
            midPoints = []
            for vertexIndex in range(len(face.vertices)):
                # find 2 vertices
                vertex1 = face.vertices[vertexIndex]
                vertex2 = face.vertices[0 if vertexIndex + 1 >= len(face.vertices) else vertexIndex + 1]
                # find average of position
                midPoint = vertex1.clone() # referance fix
                midPoint.add(vertex2)
                midPoint.scale(0.5)
                midPoints.append(midPoint)

            # the number of new faces is equal to number of vertices
            for vertexIndex in range(len(face.vertices)):
                # create faces with clockwise order
                # example of a square subdivision
                # v: vertex, m: midpoint, c: center of face
                # face1 vertices -> [v0, m01, c, m30]
                # face2 vertices -> [v1, m12, c, m01]
                # face3 vertices -> [v2, m23, c, m12]
                # face4 vertices -> [v3, m30, c, m23]
                newVertices = [face.vertices[vertexIndex], midPoints[vertexIndex], centerOfFace, midPoints[vertexIndex-1]]
                newFaces.append(Face3D(newVertices, face.color[:]))

        self.faces = newFaces

    